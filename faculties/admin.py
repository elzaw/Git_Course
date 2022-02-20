from django.contrib import admin
from faculties.models.course import Course
from faculties.models.faculty import Faculty

# Register your models here.
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    
    
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    ordering = ['id']
    