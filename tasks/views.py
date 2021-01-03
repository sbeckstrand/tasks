from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    context = {
        'title': 'Dashboard'
    }

    return render(request, 'tasks/dashboard.html', context)

def terms(request, term_id=0):
    context = {
        'title': 'Terms'
    }

    return render(request, 'tasks/terms.html', context)

def courses(request, course_id=0):
    context = {
        'title': 'Courses'
    }

    return render(request, 'tasks/courses.html', context)

def professors(request, professor_id=0):
    context = {
        'title': 'Professors'
    }

    return render(request, 'tasks/professors.html', context)

def tasks(request, task_id=0):
    context = {
        'title': 'Tasks'
    }

    return render(request, 'tasks/tasks.html', context)
