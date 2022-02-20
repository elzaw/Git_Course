
from dataclasses import fields
from unicodedata import name
from rest_framework import serializers
from faculties.models.course import Course

from faculties.models.faculty import Faculty



class EditFacultySerializer(serializers.Serializer):
   
   name = serializers.CharField()
   

        
        
class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'
        
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class EditCourseSerializer(serializers.Serializer):
    
    name = serializers.CharField()