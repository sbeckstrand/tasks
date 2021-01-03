from django.urls import path

from .import views

urlpatterns = [
    # Index Page (ex: / )
    path('', views.index, name='index'),

    # Terms (ex1: /terms/ , ex2: /terms/5 )
    path('terms/', views.terms, name="terms"),
    path('terms/<int:term_id>/', views.terms, name="terms"),

    # Courses (ex1: /courses/ , ex2: /courses/5 )
    path('courses/', views.courses, name="courses"),
    path('courses/<int:course_id>/', views.courses, name="courses"),

    # Courses (ex1: /courses/ , ex2: /courses/5 )
    path('professors/', views.professors, name="professors"),
    path('professors/<int:professor_id>/', views.professors, name="professors"),

    # Courses (ex1: /courses/ , ex2: /courses/5 )
    path('tasks/', views.tasks, name="tasks"),
    path('tasks/<int:tasks_id>/', views.tasks, name="tasks"),
]
