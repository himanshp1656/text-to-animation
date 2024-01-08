from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mailid=models.EmailField()
    subject = models.TextField(max_length=500)
    degree = models.FileField(upload_to='teacher_degrees/')
    def __str__(self) -> str:
        return self.first_name

class teacherlist(models.Model):
    name = models.CharField(max_length=100)
    description=models.TextField(max_length=10000)
    url = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.name