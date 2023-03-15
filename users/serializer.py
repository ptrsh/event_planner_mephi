from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from planner.utils import generate_jwt_token
from planner.errors import ERORRS
from planner.settings import SIMPLE_JWT
import jwt


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',
                 'password', 'email')

    def update(self, instance, validated_data):
        validated_data.pop('password', None)
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class PasswordResetSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    token = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = User
        fields = ['email', 'token']

    def update(self, instance, validated_data):
        email = validated_data.get('email', None)
        try:
            user = User.objects.get(email=email)
        except:

            raise serializers.ValidationError(ERORRS['ERROR_USER_NOT_FOUND'])

        token = generate_jwt_token(1)
        user.token = token
        user.save()
        return user

class PasswordResetConfirmSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=255)
    token = serializers.CharField(max_length=255)
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'token', 'password']

    def update(self, instance, validated_data):
        email = validated_data.get('email', None)
        password = validated_data.get('password', None)
        token = validated_data.get('token', None)

        if email is None:
            raise serializers.ValidationError(
                ERORRS['ERROR_REQUIRED']['EMAIL']
            )
        elif password is None:
            raise serializers.ValidationError(
                ERORRS['ERROR_REQUIRED']['PASSWORD']
            )
        elif token is None:
            raise serializers.ValidationError(
                ERORRS['ERROR_REQUIRED']['TOKEN']
            )

        try:
            user = User.objects.get(email=email)
        except:
            raise serializers.ValidationError(ERORRS['ERROR_USER_NOT_FOUND'])

        if not user.is_active:
            raise serializers.ValidationError(
                ERORRS['ERROR_DEACTIVATED_USER']
            )

        if user.token != token:
            raise serializers.ValidationError(
                ERORRS['ERROR_INVALID_TOKEN']
            )
        else:

            try:
                jwt.decode(token, SIMPLE_JWT['SIGNING_KEY'], algorithm='HS256')
            except:
                raise serializers.ValidationError(
                    ERORRS['ERROR_INVALID_EXPIRED']
                )

        user.set_password(password)
        user.token = None
        user.save()
        return user
