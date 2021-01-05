from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

def validate_signup(firstName, lastName, email, username, password):
    signup_errors = []

    if not (firstName.isalpha()):
        signup_errors.append("First Name contains invalid characters.")

    if not lastName.isalpha():
        signup_errors.append("Last Name contains invalid characters.")

    # Check if Email already in use and is valid
        # Need to update this to check that @ and . and TLD are provided. I believe browser only checks for @
    if len(User.objects.filter(email=email)) > 0:
        signup_errors.append("The email address '%s' is already in use." % email)

    # Check if username is already in use
    if len(User.objects.filter(username=username)) > 0:
        signup_errors.append("The username '%s' is already in use." % username)


    if not (firstName and lastName and email and username and password):
        signup_errors.append("At least one field not filled")

    if not signup_errors:
        newUser = User(first_name=firstName,last_name=lastName,username=username,email=email,password=password)
        newUser.save()

    return signup_errors

def index(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect("/dashboard")
    else:
        signup_errors = []
        validRegistration = False
        signupAttempt = False

        if request.method == "POST":
            pFirst = request.POST['firstName']
            pLast = request.POST['lastName']
            pEmail = request.POST['email']
            pUser = request.POST['username']
            pPassword = request.POST['password']

            signup_errors = validate_signup(pFirst, pLast, pEmail, pUser, pPassword)

            signupAttempt = True

        context = {
            'title': 'Tasks',
            'errors': signup_errors,
            'signupAttempt': signupAttempt
        }

        return render(request, 'tasks/index.html', context)

def signup(request):

    if request.user.is_authenticated:
        print("Testing")
        return HttpResponseRedirect("/dashboard")
    else:
        context = {
        'title': 'Signup'
        }

        return render(request, 'registration/signup.html', context)


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
