from django.db import models
from django.utils import timezone

# Models for Catigorization
class Term(models.Model):
    name = models.CharField(max_length=200)
    endDate = models.DateTimeField()
    # user = models.ForeignKey(User, one_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def is_active(self):
        return self.endDate > timezone.now()

class Professor(models.Model):
    name = models.CharField(max_length=200)
    # user = models.ForeignKey(User, one_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    prof = models.ForeignKey(Professor, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




# Models for actual Tasks
class Task(models.Model):
    title = models.CharField(max_length=200)
    priority = models.IntegerField(max_length=1)
    completed = models.BooleanField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    color = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Subtask(models.Model):
    content = models.CharField(max_length=200)
    completed = models.BooleanField()
    parent = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class Note(models.Model):
    content = models.CharField(max_length=500)
    parent = models.ForeignKey(Task, on_delete=models.CASCADE)
