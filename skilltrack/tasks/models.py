from django.db import models
from cources.models import Course

class Task(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    difficulty = models.IntegerField()
    deadline = models.DateField()

    def __str__(self):
        return self.title