# serializers.py
from rest_framework import serializers
from .models import Question,CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['firstName', 'lastName', 'email', 'username', 'password', 'country', 'phoneNumber']




class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
