from django.db import router
from django.urls import path
from auth_uni.views import AssignToFacultyView, SignInView, SignUpView,RegisterUserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user',RegisterUserViewSet,basename='users')
urlpatterns =router.urls + [
    path('users/', SignUpView.as_view()),
    path('login/',SignInView.as_view()),
    path('faculty/',AssignToFacultyView.as_view()),
    
    
]




