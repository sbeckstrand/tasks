from django.contrib import admin

from .models import Term, Course, Professor, Task, Subtask, Note

models = [Term, Course, Professor, Task, Subtask, Note]

for model in models:
    admin.site.register(model)
