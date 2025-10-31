from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)
    fullname = serializers.CharField(max_length=150, required=True, trim_whitespace=True)
    token = serializers.CharField(read_only=True)
    user_id = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["user_id", "fullname", "password", "repeated_password", "email", "token"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate_email(self, data):
        if (User.objects.filter(email=data)):
            raise serializers.ValidationError({"Error": "Email is already in use!"})
        return data

    def validate(self, data):
        if (data["password"] != data["repeated_password"]):
            raise serializers.ValidationError({"Error": "Passwords don't match!"})
        return data
    
    def create(self, validated_data):
        validated_data.pop("repeated_password", None)
        pw = validated_data.pop("password", None)
        full_name = validated_data.pop("fullname", None)
        user = User.objects.create_user(username=full_name, password=pw, **validated_data)
        token = Token.objects.create(user=user)
        user.token = token
        user.user_id = user.id
        user.fullname = full_name
        return user

 
    
        