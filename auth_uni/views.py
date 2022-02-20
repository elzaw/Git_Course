
from rest_framework.views import APIView 
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from auth_uni.models import Instructor, Student, User
from auth_uni.serializers import FacultySerializer, LoginSerializer, RegisterUserSerializer, UserSerializer
from faculties.models.faculty import Faculty
from rest_framework.permissions import IsAdminUser,IsAuthenticated

# Create your views here.

class SignUpView(APIView):
    def post(self, request):

        serialized_data = RegisterUserSerializer(data=request.data)

        if serialized_data.is_valid():
            email = serialized_data.validated_data.get('email')

            try:
                User.objects.get(email=email)
                return Response({'error': 'User with the same email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                pass

            user = User()
            user.email = email
            user.username = email
            user.set_password(serialized_data.validated_data.get('password'))
            user.first_name = serialized_data.validated_data.get('first_name')
            user.last_name = serialized_data.validated_data.get('last_name')
            user.date_of_birth = serialized_data.validated_data.get('date_of_birth')
            user.save()

            type = serialized_data.validated_data.get('type')
            if type == RegisterUserSerializer.STUDENT:
                student = Student()
                student.user = user
                student.save()
            else:
                instructor = Instructor()
                instructor.user = user
                instructor.type = type
                instructor.save()


            token = Token.objects.create(user=user)

            return Response({'message': 'User created successfully', 'data': {'user': UserSerializer(user).data, 'token': token.key}}, status=status.HTTP_200_OK)
        
        return Response({'error': 'data is not valid'}, status=status.HTTP_400_BAD_REQUEST)



class SignInView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        
        user = get_object_or_404(User,email=email)
        if user.check_password(password):
            return Response ({'message':'Loged in'})
        else: 
            return Response ({'message':'Wrong password'})
        
class RegisterUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
        
        
class AssignToFacultyView(APIView):
    permission_classes = [IsAdminUser]
    def post(self,request):
         

         serializer = FacultySerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         
         user_id = serializer.validated_data.get('user_id')
         faculty_id = serializer.validated_data.get('faculty_id')
         
         user = get_object_or_404(User,id=user_id)
         faculty = get_object_or_404(Faculty,id=faculty_id)
         
         user.faculty = faculty
         user.save()
         
         return Response ({"message":"user assigned successfully to faculty", 'data': {'user': UserSerializer(user).data}},status=status.HTTP_201_CREATED)