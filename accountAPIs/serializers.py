from rest_framework import serializers
from account.models import Account, EduDegree, Institute, DegreeName, MarkSheet, Certificate, Achievements, Address, UsefullLink
#from course.models import Course
#from noticeboard.models import NoticeBoard
#from chat.models import ChatGroup


#from rest_framework.permissions import IsAuthenticated
#from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core import signing
import hashlib
import os
import re

User = get_user_model()

from accountAPIs.mixins import MessageHandler
import random
from threading import Timer
try:
    import requests
except ModuleNotFoundError:
    requests = None
from django.core.mail import send_mail




class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','firstname', 'lastname','usertype','profile_image')



class GetUserFromUserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')




#from meeting.serializers import MeetingSerializerGET

class GeneralMeetingsSerializer(serializers.ModelSerializer):
      class Meta:
          model =  User
          fields = ('id','generalmeetings')
          depth =1 



class ContactAddSerializer(serializers.ModelSerializer):
    contactId = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['contactId']
    def update(self, instance, validated_data):
        #print ("add contact validated data: ", validated_data)
        userId = validated_data.pop('contactId', None)
        contactObj = User.objects.get(pk=int(userId));
        instance.contacts.add(contactObj);
        instance.save();
        return instance


class AchievementsSerializer(serializers.ModelSerializer):
      userId = serializers.CharField(write_only=True)
      class Meta:
           model = Achievements
           fields = ['id','name','description','startDate','endDate','userId']

      def create(self, validated_data):
        userId = validated_data.pop('userId', None)
        instance = Achievements.objects.create(**validated_data);
        instance.save();
        userObj = User.objects.get(pk=int(userId));
        userObj.achievements.add(instance)
        userObj.save()
        
        return instance


class AddressSerializer(serializers.ModelSerializer):
    userId = serializers.CharField(write_only=True)
    class Meta:
        model = Address
        fields = ['id','userId','careof','houseno','streetno','district','pincode','city','state','country','addressType']
    def create(self, validated_data):
        userId = validated_data.pop('userId', None)
        instance = Address.objects.create(**validated_data);
        instance.save();
        userObj = User.objects.get(pk=int(userId));
        userObj.addresses.add(instance)
        userObj.save()

        return instance






class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Account
        fields = ('id','firstname', 'lastname','email','username','usertype','profile_image','registrationid')


class ProfileImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = ('id','profile_image')



class OfficeIDUploadSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = ('id','officeId_doc')


class GovtID1UploadSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = ('id','govtId1_doc')


class GovtID2UploadSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = ('id','govtId2_doc')



class DOBCertUploadSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = ('id','dobCert_doc')





#govtId1_doc
#dobCert_doc




from threading import Event

class CreateAccountWithPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','username','usertype')
        model = User

    def create(self, validated_data):
        #Event().wait(5)
        #password = validated_data.pop('password', None)
        
        instance = User.objects.create(**validated_data);
        instance.save();
        fullpassword = "OLsbd!@#45"
        instance.set_password(fullpassword)
        instance.save()
        username = instance.username;
        send_mail('Registration successful! : DiCelpip'," We are glad to welcome you to DiCelpip platform!",'From <dicelpip@gmail.com>',[username])
        #print ("instance password: ", instance.password)
        return instance






def _normalize_login_id(value: str) -> str:
    return str(value or "").strip().replace(" ", "")


def _normalize_phone_digits(value: str) -> str:
    raw = _normalize_login_id(value)
    raw = raw.lstrip("+")
    raw = raw[2:] if raw.startswith("00") else raw
    digits = "".join(ch for ch in raw if ch.isdigit())
    return digits


def _mask_phone_digits(digits: str) -> str:
    if not digits:
        return ""
    tail = digits[-2:] if len(digits) >= 2 else digits
    return "*" * max(len(digits) - 2, 0) + tail


def _mask_email(email: str) -> str:
    email = _normalize_login_id(email)
    if "@" not in email:
        return email
    local, domain = email.split("@", 1)
    if not local:
        return "*@" + domain
    return (local[0] + "***@" + domain) if len(local) > 1 else (local + "*@" + domain)


def _find_user_for_login_id(login_id: str):
    login_id = _normalize_login_id(login_id)
    if not login_id:
        return None

    if "@" in login_id:
        return User.objects.filter(email__iexact=login_id).first() or User.objects.filter(username__iexact=login_id).first()

    digits = _normalize_phone_digits(login_id)
    candidates = {login_id, digits}
    if digits:
        candidates.add("+" + digits)
        if digits.startswith("91") and len(digits) == 12:
            candidates.add(digits[2:])
            candidates.add("+" + digits[2:])
        if len(digits) == 10:
            candidates.add("91" + digits)
            candidates.add("+91" + digits)

    q = None
    for c in candidates:
        q = User.objects.filter(phoneno=c) if q is None else (q | User.objects.filter(phoneno=c))
        q = q | User.objects.filter(username__iexact=c)
    return q.first() if q is not None else None


def _otp_hash(code: str) -> str:
    secret = getattr(settings, "SECRET_KEY", "")
    return hashlib.sha256(f"{code}:{secret}".encode("utf-8")).hexdigest()


def _send_sms_fast2sms(otp_code: str, phone_digits: str):
    if requests is None:
        raise serializers.ValidationError("SMS provider not available (requests not installed)")

    auth = os.environ.get("FAST2SMS_AUTHORIZATION")
    if not auth:
        raise serializers.ValidationError("FAST2SMS is not configured (FAST2SMS_AUTHORIZATION missing)")

    digits = _normalize_phone_digits(phone_digits)
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    if len(digits) != 10:
        raise serializers.ValidationError("Invalid phone number for Fast2SMS")

    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = f"variables_values={otp_code}&route=otp&numbers={digits}"
    headers = {
        "authorization": auth,
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache",
    }
    resp = requests.request("POST", url, data=payload, headers=headers, timeout=15)
    try:
        data = resp.json()
    except Exception:
        data = None
    if resp.status_code >= 400:
        raise serializers.ValidationError("SMS delivery failed (Fast2SMS)")
    if isinstance(data, dict) and data.get("return") is False:
        raise serializers.ValidationError("SMS delivery failed (Fast2SMS)")


def _send_sms_msg91(otp_code: str, phone_digits: str):
    import http.client

    authkey = os.environ.get("MSG91_AUTHKEY")
    template_id = os.environ.get("MSG91_TEMPLATE_ID")
    if not authkey or not template_id:
        raise serializers.ValidationError("MSG91 is not configured (MSG91_AUTHKEY / MSG91_TEMPLATE_ID missing)")

    digits = _normalize_phone_digits(phone_digits)
    if len(digits) == 10:
        digits = "91" + digits
    if not (digits.startswith("91") and len(digits) == 12):
        raise serializers.ValidationError("Invalid phone number for MSG91")

    conn = http.client.HTTPSConnection("control.msg91.com")
    payload = "{}"
    path = f"/api/v5/otp?template_id={template_id}&mobile={digits}&authkey={authkey}&otp={otp_code}&invisible="
    conn.request("POST", path, payload, {"Content-Type": "application/JSON"})
    res = conn.getresponse()
    if res.status >= 400:
        raise serializers.ValidationError("SMS delivery failed (MSG91)")


def _send_otp_email(otp_code: str, to_email: str):
    to_email = _normalize_login_id(to_email)
    if not to_email or "@" not in to_email:
        raise serializers.ValidationError("Invalid email")
    subject = "Your login OTP : DiracAI"
    body = f"Your OTP to login is {otp_code}"
    sender = getattr(settings, "DEFAULT_FROM_EMAIL", None) or "no-reply@localhost"
    send_mail(subject, body, sender, [to_email], fail_silently=False)


def _make_otp_token(user_id: int, otp_code: str, channel: str) -> str:
    payload = {
        "uid": int(user_id),
        "oh": _otp_hash(otp_code),
        "ch": channel,
    }
    return signing.dumps(payload, salt="accountAPIs.otp.v1")


def _load_otp_token(token: str, max_age_seconds: int):
    return signing.loads(token, salt="accountAPIs.otp.v1", max_age=max_age_seconds)


def _normalize_login_id(value: str) -> str:
    return str(value or "").strip().replace(" ", "")


def _normalize_phone_digits(value: str) -> str:
    raw = _normalize_login_id(value)
    raw = raw.lstrip("+")
    raw = raw[2:] if raw.startswith("00") else raw
    digits = "".join(ch for ch in raw if ch.isdigit())
    return digits


def _mask_phone_digits(digits: str) -> str:
    if not digits:
        return ""
    tail = digits[-2:] if len(digits) >= 2 else digits
    return "*" * max(len(digits) - 2, 0) + tail


def _mask_email(email: str) -> str:
    email = _normalize_login_id(email)
    if "@" not in email:
        return email
    local, domain = email.split("@", 1)
    if not local:
        return "*@" + domain
    return (local[0] + "***@" + domain) if len(local) > 1 else (local + "*@" + domain)


def _find_user_for_login_id(login_id: str):
    login_id = _normalize_login_id(login_id)
    if not login_id:
        return None

    if "@" in login_id:
        return User.objects.filter(email__iexact=login_id).first() or User.objects.filter(username__iexact=login_id).first()

    digits = _normalize_phone_digits(login_id)
    candidates = {login_id, digits}
    if digits:
        candidates.add("+" + digits)
        if digits.startswith("91") and len(digits) == 12:
            candidates.add(digits[2:])
            candidates.add("+" + digits[2:])
        if len(digits) == 10:
            candidates.add("91" + digits)
            candidates.add("+91" + digits)

    q = None
    for c in candidates:
        q = User.objects.filter(phoneno=c) if q is None else (q | User.objects.filter(phoneno=c))
        q = q | User.objects.filter(username__iexact=c)
    return q.first() if q is not None else None


def _otp_hash(code: str) -> str:
    secret = getattr(settings, "SECRET_KEY", "")
    return hashlib.sha256(f"{code}:{secret}".encode("utf-8")).hexdigest()


def _send_sms_fast2sms(otp_code: str, phone_digits: str):
    if requests is None:
        raise serializers.ValidationError("SMS provider not available (requests not installed)")

    auth = os.environ.get("FAST2SMS_AUTHORIZATION")
    if not auth:
        raise serializers.ValidationError("FAST2SMS is not configured (FAST2SMS_AUTHORIZATION missing)")

    digits = _normalize_phone_digits(phone_digits)
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    if len(digits) != 10:
        raise serializers.ValidationError("Invalid phone number for Fast2SMS")

    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = f"variables_values={otp_code}&route=otp&numbers={digits}"
    headers = {
        "authorization": auth,
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache",
    }
    resp = requests.request("POST", url, data=payload, headers=headers, timeout=15)
    try:
        data = resp.json()
    except Exception:
        data = None
    if resp.status_code >= 400:
        raise serializers.ValidationError("SMS delivery failed (Fast2SMS)")
    if isinstance(data, dict) and data.get("return") is False:
        raise serializers.ValidationError("SMS delivery failed (Fast2SMS)")


def _send_sms_msg91(otp_code: str, phone_digits: str):
    import http.client

    authkey = os.environ.get("MSG91_AUTHKEY")
    template_id = os.environ.get("MSG91_TEMPLATE_ID")
    if not authkey or not template_id:
        raise serializers.ValidationError("MSG91 is not configured (MSG91_AUTHKEY / MSG91_TEMPLATE_ID missing)")

    digits = _normalize_phone_digits(phone_digits)
    if len(digits) == 10:
        digits = "91" + digits
    if not (digits.startswith("91") and len(digits) == 12):
        raise serializers.ValidationError("Invalid phone number for MSG91")

    conn = http.client.HTTPSConnection("control.msg91.com")
    payload = "{}"
    path = f"/api/v5/otp?template_id={template_id}&mobile={digits}&authkey={authkey}&otp={otp_code}&invisible="
    conn.request("POST", path, payload, {"Content-Type": "application/JSON"})
    res = conn.getresponse()
    if res.status >= 400:
        raise serializers.ValidationError("SMS delivery failed (MSG91)")


def _send_otp_email(otp_code: str, to_email: str):
    to_email = _normalize_login_id(to_email)
    if not to_email or "@" not in to_email:
        raise serializers.ValidationError("Invalid email")
    subject = "Your login OTP : DiracAI"
    body = f"Your OTP to login is {otp_code}"
    sender = getattr(settings, "DEFAULT_FROM_EMAIL", None) or "no-reply@localhost"
    send_mail(subject, body, sender, [to_email], fail_silently=False)


def _make_otp_token(user_id: int, otp_code: str, channel: str) -> str:
    payload = {
        "uid": int(user_id),
        "oh": _otp_hash(otp_code),
        "ch": channel,
    }
    return signing.dumps(payload, salt="accountAPIs.otp.v1")


def _load_otp_token(token: str, max_age_seconds: int):
    return signing.loads(token, salt="accountAPIs.otp.v1", max_age=max_age_seconds)


def _normalize_login_id(value: str) -> str:
    return str(value or "").strip().replace(" ", "")


def _normalize_phone_digits(value: str) -> str:
    raw = _normalize_login_id(value)
    raw = raw.lstrip("+")
    raw = raw[2:] if raw.startswith("00") else raw
    digits = "".join(ch for ch in raw if ch.isdigit())
    return digits


def _mask_phone_digits(digits: str) -> str:
    if not digits:
        return ""
    tail = digits[-2:] if len(digits) >= 2 else digits
    return "*" * max(len(digits) - 2, 0) + tail


def _mask_email(email: str) -> str:
    email = _normalize_login_id(email)
    if "@" not in email:
        return email
    local, domain = email.split("@", 1)
    if not local:
        return "*@" + domain
    return (local[0] + "***@" + domain) if len(local) > 1 else (local + "*@" + domain)


def _find_user_for_login_id(login_id: str):
    login_id = _normalize_login_id(login_id)
    if not login_id:
        return None

    if "@" in login_id:
        return User.objects.filter(email__iexact=login_id).first() or User.objects.filter(username__iexact=login_id).first()

    digits = _normalize_phone_digits(login_id)
    candidates = {login_id, digits}
    if digits:
        candidates.add("+" + digits)
        if digits.startswith("91") and len(digits) == 12:
            candidates.add(digits[2:])
            candidates.add("+" + digits[2:])
        if len(digits) == 10:
            candidates.add("91" + digits)
            candidates.add("+91" + digits)

    q = None
    for c in candidates:
        q = User.objects.filter(phoneno=c) if q is None else (q | User.objects.filter(phoneno=c))
        q = q | User.objects.filter(username__iexact=c)
    return q.first() if q is not None else None


def _otp_hash(code: str) -> str:
    secret = getattr(settings, "SECRET_KEY", "")
    return hashlib.sha256(f"{code}:{secret}".encode("utf-8")).hexdigest()


def _send_sms_fast2sms(otp_code: str, phone_digits: str):
    if requests is None:
        raise serializers.ValidationError("SMS provider not available (requests not installed)")

    auth = os.environ.get("FAST2SMS_AUTHORIZATION")
    if not auth:
        raise serializers.ValidationError("FAST2SMS is not configured (FAST2SMS_AUTHORIZATION missing)")

    digits = _normalize_phone_digits(phone_digits)
    if digits.startswith("91") and len(digits) == 12:
        digits = digits[2:]
    if len(digits) != 10:
        raise serializers.ValidationError("Invalid phone number for Fast2SMS")

    url = "https://www.fast2sms.com/dev/bulkV2"
    payload = f"variables_values={otp_code}&route=otp&numbers={digits}"
    headers = {
        "authorization": auth,
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache",
    }
    resp = requests.request("POST", url, data=payload, headers=headers, timeout=15)
    try:
        data = resp.json()
    except Exception:
        data = None
    if resp.status_code >= 400:
        raise serializers.ValidationError("SMS delivery failed (Fast2SMS)")
    if isinstance(data, dict) and data.get("return") is False:
        raise serializers.ValidationError("SMS delivery failed (Fast2SMS)")


def _send_sms_msg91(otp_code: str, phone_digits: str):
    import http.client

    authkey = os.environ.get("MSG91_AUTHKEY")
    template_id = os.environ.get("MSG91_TEMPLATE_ID")
    if not authkey or not template_id:
        raise serializers.ValidationError("MSG91 is not configured (MSG91_AUTHKEY / MSG91_TEMPLATE_ID missing)")

    digits = _normalize_phone_digits(phone_digits)
    if len(digits) == 10:
        digits = "91" + digits
    if not (digits.startswith("91") and len(digits) == 12):
        raise serializers.ValidationError("Invalid phone number for MSG91")

    conn = http.client.HTTPSConnection("control.msg91.com")
    payload = "{}"
    path = f"/api/v5/otp?template_id={template_id}&mobile={digits}&authkey={authkey}&otp={otp_code}&invisible="
    conn.request("POST", path, payload, {"Content-Type": "application/JSON"})
    res = conn.getresponse()
    if res.status >= 400:
        raise serializers.ValidationError("SMS delivery failed (MSG91)")


def _send_otp_email(otp_code: str, to_email: str):
    to_email = _normalize_login_id(to_email)
    if not to_email or "@" not in to_email:
        raise serializers.ValidationError("Invalid email")
    subject = "Your login OTP : DiracAI"
    body = f"Your OTP to login is {otp_code}"
    sender = getattr(settings, "DEFAULT_FROM_EMAIL", None) or "no-reply@localhost"
    send_mail(subject, body, sender, [to_email], fail_silently=False)


def _make_otp_token(user_id: int, otp_code: str, channel: str) -> str:
    payload = {
        "uid": int(user_id),
        "oh": _otp_hash(otp_code),
        "ch": channel,
    }
    return signing.dumps(payload, salt="accountAPIs.otp.v1")


def _load_otp_token(token: str, max_age_seconds: int):
    return signing.loads(token, salt="accountAPIs.otp.v1", max_age=max_age_seconds)


def changePasswordAfter(userObj):
    return None; 


class AccountOTPRequestSerializer(serializers.Serializer):
    login_id = serializers.CharField()
    channel = serializers.ChoiceField(choices=[("sms", "sms"), ("email", "email"), ("both", "both")], default="both")
    sms_provider = serializers.ChoiceField(choices=[("fast2sms", "fast2sms"), ("msg91", "msg91")], required=False, allow_null=True)

    def create(self, validated_data):
        login_id = validated_data["login_id"]
        channel = validated_data.get("channel") or "both"
        sms_provider = validated_data.get("sms_provider")

        user = _find_user_for_login_id(login_id)
        if not user:
            raise serializers.ValidationError({"login_id": "User not found"})

        ttl = int(getattr(settings, "ACCOUNT_OTP_TTL_SECONDS", 600))
        otp_code = f"{random.randint(100000, 999999)}"
        token = _make_otp_token(user.id, otp_code, channel)

        sms_sent = False
        email_sent = False
        errors = []

        if channel in ("sms", "both"):
            try:
                target_phone = getattr(user, "phoneno", None) or getattr(user, "username", None) or ""
                if sms_provider == "msg91":
                    _send_sms_msg91(otp_code, target_phone)
                else:
                    _send_sms_fast2sms(otp_code, target_phone)
                sms_sent = True
            except Exception as exc:
                errors.append(f"sms: {str(exc)}")

        if channel in ("email", "both"):
            try:
                _send_otp_email(otp_code, getattr(user, "email", "") or login_id)
                email_sent = True
            except Exception as exc:
                errors.append(f"email: {str(exc)}")

        destination = _mask_email(user.email) if "@" in (getattr(user, "email", "") or "") else _mask_phone_digits(_normalize_phone_digits(getattr(user, "phoneno", "")))

        return {
            "success": True,
            "otp_token": token,
            "sms_sent": sms_sent,
            "email_sent": email_sent,
            "destination": destination,
            "expires_in_seconds": ttl,
            "errors": errors,
            **({"otp_debug": otp_code} if getattr(settings, "DEBUG", False) else {}),
        }


class AccountOTPVerifySerializer(serializers.Serializer):
    otp_token = serializers.CharField()
    otp_code = serializers.CharField()

    def validate(self, attrs):
        ttl = int(getattr(settings, "ACCOUNT_OTP_TTL_SECONDS", 600))
        code = _normalize_login_id(attrs.get("otp_code"))
        if not re.fullmatch(r"\d{4,8}", code):
            raise serializers.ValidationError({"otp_code": "Invalid OTP format"})

        try:
            payload = _load_otp_token(attrs.get("otp_token"), ttl)
        except signing.SignatureExpired:
            raise serializers.ValidationError({"otp_token": "OTP expired"})
        except signing.BadSignature:
            raise serializers.ValidationError({"otp_token": "Invalid OTP token"})

        if payload.get("oh") != _otp_hash(code):
            raise serializers.ValidationError({"otp_code": "Invalid OTP"})

        user = User.objects.filter(id=payload.get("uid")).first()
        if not user:
            raise serializers.ValidationError({"otp_token": "User not found"})

        attrs["user"] = user
        return attrs
 


class AccountOTPRequestSerializer(serializers.Serializer):
    login_id = serializers.CharField()
    channel = serializers.ChoiceField(choices=[("sms", "sms"), ("email", "email"), ("both", "both")], default="both")
    sms_provider = serializers.ChoiceField(choices=[("fast2sms", "fast2sms"), ("msg91", "msg91")], required=False, allow_null=True)

    def create(self, validated_data):
        login_id = validated_data["login_id"]
        channel = validated_data.get("channel") or "both"
        sms_provider = validated_data.get("sms_provider")

        user = _find_user_for_login_id(login_id)
        if not user:
            raise serializers.ValidationError({"login_id": "User not found"})

        ttl = int(getattr(settings, "ACCOUNT_OTP_TTL_SECONDS", 600))
        otp_code = f"{random.randint(100000, 999999)}"
        token = _make_otp_token(user.id, otp_code, channel)

        sms_sent = False
        email_sent = False
        errors = []

        if channel in ("sms", "both"):
            try:
                target_phone = getattr(user, "phoneno", None) or getattr(user, "username", None) or ""
                if sms_provider == "msg91":
                    _send_sms_msg91(otp_code, target_phone)
                else:
                    _send_sms_fast2sms(otp_code, target_phone)
                sms_sent = True
            except Exception as exc:
                errors.append(f"sms: {str(exc)}")

        if channel in ("email", "both"):
            try:
                _send_otp_email(otp_code, getattr(user, "email", "") or login_id)
                email_sent = True
            except Exception as exc:
                errors.append(f"email: {str(exc)}")

        destination = _mask_email(user.email) if "@" in (getattr(user, "email", "") or "") else _mask_phone_digits(_normalize_phone_digits(getattr(user, "phoneno", "")))

        return {
            "success": True,
            "otp_token": token,
            "sms_sent": sms_sent,
            "email_sent": email_sent,
            "destination": destination,
            "expires_in_seconds": ttl,
            "errors": errors,
            **({"otp_debug": otp_code} if getattr(settings, "DEBUG", False) else {}),
        }


class AccountOTPVerifySerializer(serializers.Serializer):
    otp_token = serializers.CharField()
    otp_code = serializers.CharField()

    def validate(self, attrs):
        ttl = int(getattr(settings, "ACCOUNT_OTP_TTL_SECONDS", 600))
        code = _normalize_login_id(attrs.get("otp_code"))
        if not re.fullmatch(r"\d{4,8}", code):
            raise serializers.ValidationError({"otp_code": "Invalid OTP format"})

        try:
            payload = _load_otp_token(attrs.get("otp_token"), ttl)
        except signing.SignatureExpired:
            raise serializers.ValidationError({"otp_token": "OTP expired"})
        except signing.BadSignature:
            raise serializers.ValidationError({"otp_token": "Invalid OTP token"})

        if payload.get("oh") != _otp_hash(code):
            raise serializers.ValidationError({"otp_code": "Invalid OTP"})

        user = User.objects.filter(id=payload.get("uid")).first()
        if not user:
            raise serializers.ValidationError({"otp_token": "User not found"})

        attrs["user"] = user
        return attrs
 


class AccountOTPRequestSerializer(serializers.Serializer):
    login_id = serializers.CharField()
    channel = serializers.ChoiceField(choices=[("sms", "sms"), ("email", "email"), ("both", "both")], default="both")
    sms_provider = serializers.ChoiceField(choices=[("fast2sms", "fast2sms"), ("msg91", "msg91")], required=False, allow_null=True)

    def create(self, validated_data):
        login_id = validated_data["login_id"]
        channel = validated_data.get("channel") or "both"
        sms_provider = validated_data.get("sms_provider")

        user = _find_user_for_login_id(login_id)
        if not user:
            raise serializers.ValidationError({"login_id": "User not found"})

        ttl = int(getattr(settings, "ACCOUNT_OTP_TTL_SECONDS", 600))
        otp_code = f"{random.randint(100000, 999999)}"
        token = _make_otp_token(user.id, otp_code, channel)

        sms_sent = False
        email_sent = False
        errors = []

        if channel in ("sms", "both"):
            try:
                target_phone = getattr(user, "phoneno", None) or getattr(user, "username", None) or ""
                if sms_provider == "msg91":
                    _send_sms_msg91(otp_code, target_phone)
                else:
                    _send_sms_fast2sms(otp_code, target_phone)
                sms_sent = True
            except Exception as exc:
                errors.append(f"sms: {str(exc)}")

        if channel in ("email", "both"):
            try:
                _send_otp_email(otp_code, getattr(user, "email", "") or login_id)
                email_sent = True
            except Exception as exc:
                errors.append(f"email: {str(exc)}")

        destination = _mask_email(user.email) if "@" in (getattr(user, "email", "") or "") else _mask_phone_digits(_normalize_phone_digits(getattr(user, "phoneno", "")))

        return {
            "success": True,
            "otp_token": token,
            "sms_sent": sms_sent,
            "email_sent": email_sent,
            "destination": destination,
            "expires_in_seconds": ttl,
            "errors": errors,
            **({"otp_debug": otp_code} if getattr(settings, "DEBUG", False) else {}),
        }


class AccountOTPVerifySerializer(serializers.Serializer):
    otp_token = serializers.CharField()
    otp_code = serializers.CharField()

    def validate(self, attrs):
        ttl = int(getattr(settings, "ACCOUNT_OTP_TTL_SECONDS", 600))
        code = _normalize_login_id(attrs.get("otp_code"))
        if not re.fullmatch(r"\d{4,8}", code):
            raise serializers.ValidationError({"otp_code": "Invalid OTP format"})

        try:
            payload = _load_otp_token(attrs.get("otp_token"), ttl)
        except signing.SignatureExpired:
            raise serializers.ValidationError({"otp_token": "OTP expired"})
        except signing.BadSignature:
            raise serializers.ValidationError({"otp_token": "Invalid OTP token"})

        if payload.get("oh") != _otp_hash(code):
            raise serializers.ValidationError({"otp_code": "Invalid OTP"})

        user = User.objects.filter(id=payload.get("uid")).first()
        if not user:
            raise serializers.ValidationError({"otp_token": "User not found"})

        attrs["user"] = user
        return attrs





class CreateOTPAccountWithPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','username')
        model = User

    def update(self, instance, validated_data):
        username=validated_data.pop('username', None)
        username = username.replace(" ", "")
        userObj = User.objects.get(username=username)
        otp = random.randint(10000,99999)
        fullpassword = 'OLsbd!@#45'+ str(otp)
        userObj.set_password(fullpassword)
        userObj.save()
        #mob10digitNum= username[3:]
        #url = "https://www.fast2sms.com/dev/bulkV2"
        #payload = "variables_values={0}&route=otp&numbers={1}".format(otp, mob10digitNum);
        #headers = {
        #  'authorization': "CqDtUWF4wjpv5brzxXPlaOic2IZS6GYkNLdy7hKfJM9A10BguEDiG0mLEcxyKnApUqMaCu7Jl1eRbF9o",
        #  'Content-Type': "application/x-www-form-urlencoded",
        #  'Cache-Control': "no-cache",
        #}
        #response = requests.request("POST", url, data=payload, headers=headers)
        #otpObj = MessageHandler(username,otp)
        #otpObj.send_otp_on_phone()
        print ("usename ------------------------",username)
        #html_message = render_to_string('account/mail_template.html')
        #plain_message = strip_tags(html_message)
        #send_mail('Registration successful!',plain_message,'From <edresearch.in@gmail.com>',[email],html_message=html_message)
        send_mail('OTP : DiCelpip',str(otp),'From <dicelpip@gmail.com>',[username])

        return instance


#classes = ClassSerializer(many=True)


class DegreeNameSerializer(serializers.ModelSerializer):
      class Meta:
          model = DegreeName
          fields = '__all__'

class InstituteSerializer(serializers.ModelSerializer):
      class Meta:
          model = Institute
          fields = '__all__'


class MarkSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkSheet
        fields = '__all__'



class CertificateSerializer(serializers.ModelSerializer):
      class Meta:
        model = Certificate
        fields = '__all__'



class EduDegreeSerializer(serializers.ModelSerializer):
      institute = InstituteSerializer();
      degreename = DegreeNameSerializer();
      #marksheets = MarkSheetSerializer(many=True);
      #certificates = CertificateSerializer(many=True);
      class Meta:
          model = EduDegree
          fields = ['id','institute','degreename', 'startDate','endDate']

      #def get_institute(self, instance):
      #    return instance.institute.name

      #def get_degreename(self,instance):
      #    return instance.degreename



class EduDegreeCreateSerializer(serializers.ModelSerializer):
    #userId = serializers.SerializerMethodField()
    userId = serializers.CharField(write_only=True)
    institute = serializers.CharField(write_only=True)
    class Meta:
        model = EduDegree
        fields = ['userId','institute','degreename', 'startDate','endDate']

    def create(self, validated_data):
        userid = validated_data.pop('userId', None)
        userInstance = User.objects.get(pk=userid)
        #institute=validated_data['institute']
        institute = validated_data.pop('institute', None);
        instance = EduDegree.objects.create(**validated_data);

        if institute.isdigit():
           instituteObj = Institute.objects.get(pk=institute);
           instance.institute=instituteObj
           instance.save()
        if not institute.isdigit():    
           instData = {"name":institute}
           dummyInstitute=Institute.objects.create(**instData)
           dummyInstitute.dummy = "yes"  
           instance.institute=dummyInstitute
           instance.save()
        print ("institute: ", institute)
        print ("type of institute: ", type(institute))   
        userInstance.educationDegrees.add(instance)
        userInstance.save();
        return instance;


#class DegreeNameSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = DegreeName
#        fields = ['id','name']


#class Institute




#Institute, DegreeName, MarkSheet, Certificate



class ContactSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = '__all__'

#from rest_framework.fields import CurrentUserDefault


class TeacherSerializer2(serializers.ModelSerializer):
     usertitle = serializers.SerializerMethodField() 
     class Meta:
         fields = ('id', 'username','usertitle', 'firstname','lastname','profile_image')
         model = User
     def get_usertitle(self, instance):
        #userObj = self.context['request'].user
        #print ("user: ", userObj)
        if instance.usertitle is None:
            return None;
        return instance.usertitle.name    







#class CourseEnrollRequestObjectSerializer(serializers.Serializer):
#       usertitle = serializers.SerializerMethodField()


class UserSerializer(serializers.ModelSerializer):
   usertitle = serializers.SerializerMethodField()
   educationDegrees = EduDegreeSerializer(many=True)
   contacts = ContactSerializer(many=True)
   achievements = AchievementsSerializer(many=True)
   addresses = AddressSerializer(many=True)

   class Meta:
      model = User
      fields = ['id','usertitle','firstname', 'lastname','email','username','usertype','profile_image','registrationid','gender','position','dateofbirth','institute','city','state','country','officeId_doc','govtId1_doc','govtId2_doc','dobCert_doc','educationDegrees','contacts','achievements','addresses']
   def get_usertitle(self, instance):
        if instance.usertitle is None:
            return None;
        return instance.usertitle.name


            
class UserProfileSerializer(serializers.ModelSerializer):
      #usertitle = serializers.SerializerMethodField()
      class Meta:
          model = User
          fields = ['id','usertitle','firstname', 'lastname','email','username', 'gender','position','dateofbirth', 'institute','city', 'state','country' ]
      #def get_usertitle(self, instance):
      #  if instance.usertitle is None:
      #      return None;
      #  return instance.usertitle.name






class UserSerializerFew(serializers.ModelSerializer):
      class Meta:
          model = User
          fields = ['id','firstname', 'lastname','username','profile_image','usertype']



class InstituteSerializerForSearch(serializers.ModelSerializer):
      class Meta:
          model = Institute
          fields = ['id','name']

















class CreateUseFullLinkSerializer(serializers.ModelSerializer):
      name = serializers.CharField(write_only=True)
      link = serializers.CharField(write_only=True)
      description = serializers.CharField(write_only=True)
      class Meta:
          fields = ('id','name','link','description')
          model = User

      def update(self, instance, validated_data):
        newLinkObj = CourseLink.objects.create(**validated_data)
        instance.courselinks.add(newLinkObj)
        instance.save()
        return instance


class UseFullLinkSerializer(serializers.ModelSerializer):
      class Meta:
          fields = ('id','name','link','description')
          model = UsefullLink 

      def create(self, validated_data):
          loggedInUser = self.context['request'].user;
          newLinkObj = UsefullLink.objects.create(**validated_data)
          loggedInUser.usefull_links.add(newLinkObj)
          loggedInUser.save();
          return newLinkObj;


