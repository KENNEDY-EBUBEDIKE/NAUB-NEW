from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from .models import User
from rest_framework import serializers


class MyAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        password = attrs.get('password')
        email = attrs.get('email')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Email or password is incorrect')
                raise serializers.ValidationError(detail=msg)
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(detail=msg)
        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'privilege']

    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         email=validated_data['email'],
    #         username=validated_data['username'],
    #         password=validated_data['password'],
    #     )
    #     user.first_name = validated_data['first_name']
    #     user.last_name = validated_data['last_name']
    #     user.photo = validated_data['photo']
    #     user.save()
    #     return user

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.photo = validated_data.get('photo', instance.photo)
    #     instance.save()
    #     return instance
