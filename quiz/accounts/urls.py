from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path('questions/', views.QuestionView.as_view(), name='question-api'),
    path('register/', views.Register.as_view(), name='register-api'),
    path('login/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

