from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from faculties.models.course import Course
from faculties.models.faculty import Faculty
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated , IsAuthenticatedOrReadOnly
from faculties.serializers import CourseSerializer, EditCourseSerializer, EditFacultySerializer , FacultySerializer
# Create your views here.

class FacultyView(APIView):
    def post(self,request):
        
        serializer = EditFacultySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        faculty_name = serializer.validated_data.get('name')
        
        try:
         Faculty.objects.get(name=faculty_name)
         return Response({'error':'Faculty with the same name is already excits.'},status=status.HTTP_400_BAD_REQUEST)
        
        except Faculty.DoesNotExist:
            faculty = Faculty(name=faculty_name)
            faculty.save()
            return Response({'message':'Faculty added succsessfully. '},status=status.HTTP_201_CREATED)
    
    def get(self,requst):
        faculties = Faculty.objects.all()
        serializer = FacultySerializer(faculties,many=True)           
        
        return Response (serializer.data)
    
    
    
    
class FacultyDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,requst,pk):
        
        faculty = get_object_or_404(Faculty,pk=pk)
        serializer = FacultySerializer(faculty)
        return Response(serializer.data)
        
    def delete(self,request,pk):
        faculty = get_object_or_404(Faculty ,pk=pk)
        faculty.delete()
        return Response({'message':'Course deleted succsessfully. '},status=status.HTTP_204_NO_CONTENT)
    
    def patch(self,request,pk):
        serializer = EditFacultySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        name = serializer.validated_data.get('name')
        
        faculty = get_object_or_404(Faculty,pk=pk)
        faculty.name=name
        faculty.save()
        return Response({'message':'Faculty Updated succsessfully. '},status=status.HTTP_202_ACCEPTED)
        
    
    
    
class CourseView(APIView):
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        course_name = serializer.validated_data.get('name')
        
        try:
            Course.objects.get(name=course_name)
            return Response({'error':'Course with the same name is already excits.'},status=status.HTTP_400_BAD_REQUEST)
        
        except Course.DoesNotExist:
            course = Course(name=course_name)
            course.save()
            return Response({'message':'Course added succsessfully. '},status=status.HTTP_201_CREATED)

    
    def get(self,requst):
        courseres = Course.objects.all()
        serializer = CourseSerializer(courseres,many=True)           
        return Response (serializer.data)
    
    
class CourseDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self,requst,pk):
        course = get_object_or_404(Course,pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
        
    
    def delete(self,request,pk):
        course = get_object_or_404(Course ,id=pk)
        course.delete()
        return Response({'message':'Course deleted succsessfully. '},status=status.HTTP_204_NO_CONTENT)
            
    def patch(self,request,pk):
        serializer = EditCourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
    
        name = serializer.validated_data.get('name')
        
        faculty = get_object_or_404(Course,pk=pk)
        faculty.name=name
        faculty.save()
        return Response({'message':'Course Updated succsessfully. '},status=status.HTTP_202_ACCEPTED)