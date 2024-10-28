from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'first_name', 'last_name', 'phone_number'] 
        extra_kwargs = {'password': {'write_only': True}}






    def validate_password(self, value):
        validate_password(value)
        return value



    def create(self, validated_data):

        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            phone_number=validated_data.get('phone_number', None)
        )
        return user  # Return the user instance here




