from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

# 1. Регистрация
# 2. Активация
# 3. login
# 4. Востановление пароля
# 5. Смена пароля
# 6, Профиль пользователя


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Вам на почту отпрален код подтверждения', status=status.HTTP_201_CREATED)


class ActivationView(APIView):
    def post(self, request):
        serializer = ActivationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Ваш аккаунт успешно актевирован', status=status.HTTP_200_OK)


class LoginView():



class LogoutView(APIView):
    pass


class ResetPasswordView(APIView):
    pass


class ChangePasswordView(APIView):
    pass


class UserProfileView(APIView):
    pass

