from rest_framework import status
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import EmailMessage

from .models import User
from .serializer import UserSerializer, RegistrationSerializer, PasswordResetSerializer, PasswordResetConfirmSerializer


class UserView(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data

        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class ResetPasswordAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = self.serializer_class(
            {}, data=serializer_data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data

        recipient_email = data['email']
        email = EmailMessage('Reset Password request for Event Manager', request.build_absolute_uri()
                             + '?token=' + data['token'] + '&email=' + recipient_email, to=[recipient_email])
        email.send()

        return Response('Successfully sent reset password link to email: ' + data['email'], status=status.HTTP_200_OK)


class ResetPasswordConfirmAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = self.serializer_class(
            {}, data=serializer_data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Password has been successfully reset', status=status.HTTP_200_OK)
