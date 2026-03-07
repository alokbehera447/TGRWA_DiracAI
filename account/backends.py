

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

class CaseInsensitiveModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        # Accept username, email, or phone number as identifier
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or str(username).strip() == "" or password is None:
            return None
        username = str(username).strip()

        user = (
            UserModel.objects.filter(
                Q(username__iexact=username)
                | Q(email__iexact=username)
                | Q(phoneno__iexact=username)
            )
            .order_by("id")
            .first()
        )
        if not user:
            UserModel().set_password(password)
            return None
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None


















