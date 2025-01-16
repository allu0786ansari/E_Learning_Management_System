from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from userauths.models import User, Profile
from django.contrib.auth.password_validation import validate_password
from django.utils.text import slugify
from django.db.models import Max

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['full_name'] = user.full_name
        token['email'] = user.email
        token['username'] = user.username
        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['full_name', 'email', 'username', 'password', 'password2']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate(self, attrs):
        try:
            validate_password(attrs['password'])
        except serializers.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})
        
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password2": "Passwords didn't match."})
        return attrs

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            full_name=validated_data['full_name']
        )
        email_username = slugify(validated_data['email'].split('@')[0])
        # Ensure unique username
        max_suffix = User.objects.filter(username__startswith=email_username).aggregate(Max('username'))['username__max']
        if max_suffix:
            email_username += str(int(max_suffix.split(email_username)[-1]) + 1)
        user.username = email_username
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'