from rest_framework import serializers
from .models import Account
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


class TokenSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label=_("Email"),
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
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            account = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not account:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['email'] = account
        return attrs


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'password', "first_name", "last_name"]
        extra_kwargs = {'password': {'write_only': True}}


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, write_only=True)
    first_name = serializers.CharField(required=True, max_length=40)
    last_name = serializers.CharField(required=True, max_length=40)
    
    class Meta:
        model = Account
        fields = ["id", "email", "password", 'password2', 'first_name', "last_name"]
        extra_kwargs = {'password': {'write_only': True}}

    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('passwords do not match')
        return data
    
    def create(self, validated_data):
        account = Account(
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name')
            )
        account.set_password(validated_data['password'])
        account.save()
        return account

        
