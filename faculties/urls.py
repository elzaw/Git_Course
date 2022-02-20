from django.urls import path

from faculties.views import CourseView, FacultyView, CourseDetailView, FacultyDetailView 



urlpatterns = [
    path('faculties/',FacultyView.as_view()),
    path('courses/',CourseView.as_view()),
    path('faculties/<int:pk>/',FacultyDetailView.as_view()),
    path('courses/<int:pk>/',CourseDetailView.as_view()),
    
    
]