from django.shortcuts import render



# Dashboard View
def dashboard(request):

    context = {

        'total_students': 350,

        'total_courses': 25,

        'total_lecturers': 40,

        'total_departments': 8,

    }

    return render(
        request,
        'dashboard.html',
        context
    )




# Students View
def students(request):

    students_data = [

        {
            'id': '001',
            'name': 'John Peter',
            'course': 'Computer Science',
            'year': '2'
        },


        {
            'id': '002',
            'name': 'Asha Ali',
            'course': 'Information Technology',
            'year': '1'
        },


        {
            'id': '003',
            'name': 'Michael James',
            'course': 'Computer Systems',
            'year': '3'
        }

    ]


    return render(
        request,
        'students.html',
        {
            'students': students_data
        }
    )




# Courses View
def courses(request):

    courses_data = [

        {
            'code': 'CS101',
            'name': 'Computer Science',
            'duration': '3 Years'
        },


        {
            'code': 'IT201',
            'name': 'Information Technology',
            'duration': '3 Years'
        }

    ]


    return render(
        request,
        'courses.html',
        {
            'courses': courses_data
        }
    )




# Lecturers View
def lecturers(request):

    lecturers_data = [

        {
            'id': '001',
            'name': 'Dr. John',
            'department': 'Computer Science'
        },


        {
            'id': '002',
            'name': 'Dr. Mary',
            'department': 'Information Technology'
        }

    ]


    return render(
        request,
        'lecturers.html',
        {
            'lecturers': lecturers_data
        }
    )




# Departments View
def departments(request):

    departments_data = [

        {
            'id': '01',
            'name': 'Computer Science'
        },


        {
            'id': '02',
            'name': 'Information Technology'
        }

    ]


    return render(
        request,
        'departments.html',
        {
            'departments': departments_data
        }
    )




# Profile View
def profile(request):

    profile_data = {

        'name': 'Amani Selemani',

        'registration': '33755/T.2024',

        'course': 'Computer Systems and Networks'

    }


    return render(
        request,
        'profile.html',
        {
            'profile': profile_data
        }
    )




# Settings View
def settings(request):

    return render(
        request,
        'settings.html'
    )