from rest_framework import serializers
from django.contrib.auth.models import User

class SignInSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user
