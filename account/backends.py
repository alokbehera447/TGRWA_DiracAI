# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend


# class CaseInsensitiveModelBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         if username is None:
#             username = kwargs.get(UserModel.USERNAME_FIELD)
#         try:
#             case_insensitive_username_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
#             user = UserModel._default_manager.get(**{case_insensitive_username_field: username})
#         except UserModel.DoesNotExist:
#             # Run the default password hasher once to reduce the timing
#             # difference between an existing and a non-existing user (#20760).
#             UserModel().set_password(password)
#         else:
#             if user.check_password(password) and self.user_can_authenticate(user):
#                 return user


from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

class CaseInsensitiveModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        # Accept username, email, or phone number as identifier
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        try:
            user = UserModel.objects.get(
                Q(username__iexact=username) |
                Q(email__iexact=username) |
                Q(phoneno__iexact=username)
            )
        except UserModel.DoesNotExist:
            # Avoid timing attack — call password hasher even if user not found
            UserModel().set_password(password)
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user


















