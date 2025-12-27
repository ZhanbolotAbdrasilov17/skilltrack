from django.db import models
from student.models import Student
from tasks.models import Task

class Progress(models.Model):
    STATUS_CHOICES = [
        ('new', 'Не начато'),
        ('done', 'Выполнено'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    updated_at = models.DateTimeField(auto_now=True)