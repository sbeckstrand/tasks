from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

def index(request):

    context = {
        'title': 'Tasks'
    }

    return render(request, 'tasks/index.html', context)

@login_required
def profile(request):
    context = {

    'title': 'Profile'

    }

    return render(request, 'tasks/profile.html', context)

@login_required
def dashboard(request):

    context = {
        'title': 'Dashboard'
    }

    return render(request, 'tasks/dashboard.html', context)

@login_required
def terms(request, term_id=0):
    context = {
        'title': 'Terms'
    }

    return render(request, 'tasks/terms.html', context)

@login_required
def courses(request, course_id=0):
    context = {
        'title': 'Courses'
    }

    return render(request, 'tasks/courses.html', context)

@login_required
def professors(request, professor_id=0):
    context = {
        'title': 'Professors'
    }

    return render(request, 'tasks/professors.html', context)

@login_required
def tasks(request, task_id=0):
    context = {
        'title': 'Tasks'
    }

    return render(request, 'tasks/tasks.html', context)
