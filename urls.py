from django.urls import path
from . import views


urlpatterns = [

    # Dashboard
    path('', views.dashboard, name='dashboard'),


    # Students page
    path('students/', views.students, name='students'),


    # Courses page
    path('courses/', views.courses, name='courses'),


    # Lecturers page
    path('lecturers/', views.lecturers, name='lecturers'),


    # Departments page
    path('departments/', views.departments, name='departments'),


    # Profile page
    path('profile/', views.profile, name='profile'),


    # Settings page
    path('settings/', views.settings, name='settings'),

]