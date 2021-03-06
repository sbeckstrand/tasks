from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django import forms
from .forms import SignupForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .models import Term

from datetime import datetime

def index(request):

    template = ""
    tite = ""
    successfulSignup = False

    if request.user.is_authenticated:
        return HttpResponseRedirect("/dashboard")
    else:

        if request.method == "POST":
            form = SignupForm(request.POST)
            if form.is_valid():
                firstName = form.cleaned_data['first_name']
                lastName = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                newUser = User.objects.create_user(first_name=firstName,last_name=lastName,email=email,username=username,password=password)
                newUser.save()

                successfulSignup = True

        else:
            form = SignupForm()

        if request.path == '/signup/':
            template = "registration/signup.html"
            title = "Signup"
        else:
            title = "Tasks"
            template = "tasks/index.html"

        context = {
            'title': title,
            'successfulSignup': successfulSignup,
            'form': form
        }

        return render(request, template, context)


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

    if term_id == 0:
        terms = Term.objects.filter(user_id=request.user.id)
        active_term = ""

        try:
            active_term = terms.filter(endDate__gt=datetime.now())[0]
        except:
            active_terms = ""

        expired_terms = terms.filter(endDate__lt=datetime.now())
        
        print(len(expired_terms))

        context = {
            'title': 'Terms',
            'active_term': active_term,
            'expired_terms': expired_terms,
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
