# views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionSerializer,CustomUserSerializer
from django.contrib.auth import authenticate
from.models import Question
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

class Register(APIView):
    def post(self, request):
        print(request.data)
        serializer = CustomUserSerializer(data=request.data)
        print(88888888888888888888888888888888888888)
        if serializer.is_valid():
            print(9999999999999999999999999999999999999)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TokenObtainPairView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        print(888888888888888,username,password)
        user = authenticate(username=username, password=password)
 
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            })
        else:
            return Response({"error": "Invalid credentials"}, status=401)



class QuestionView(APIView):
    def post(self,request):
        serializer=QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        categories = Question.objects.all()
        serializer=QuestionSerializer(categories,many=True)
        return Response(serializer.data)
        