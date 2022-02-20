
from dataclasses import fields
from pyexpat import model
from .models import User
from rest_framework import serializers
class RegisterUserSerializer(serializers.Serializer):

    STUDENT = 'Student'
    PROFESSOR = 'Professor'
    TEACHING_ASSISTANT = 'TA'
    USER_TYPE_CHOICES = (
        (STUDENT, 'Student'),
        (PROFESSOR, 'Professor'),
        (TEACHING_ASSISTANT, 'TA'),
    )

    email = serializers.EmailField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    date_of_birth = serializers.DateField()
    type = serializers.ChoiceField(choices=USER_TYPE_CHOICES)
    
   

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','password','first_name','last_name','email','date_of_birth','faculty']
        
class LoginSerializer (serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
class AllUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
class FacultySerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    faculty_id = serializers.IntegerField()