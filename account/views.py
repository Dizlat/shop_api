from django.shortcuts import render
from rest_framework.views import APIView


# 1. Регистрация
# 2. Активация
# 3. login
# 4. Востановление пароля
# 5. Смена пароля
# 6, Профиль пользователя


class RegisterView(APIView):
    pass


class ActivationView(APIView):
    pass


class LoginView():
    pass


class LogoutView(APIView):
    pass


class ResetPasswordView(APIView):
    pass


class ChangePasswordView(APIView):
    pass


class UserProfileView(APIView):
    pass

