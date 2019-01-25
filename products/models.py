from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
    Title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    body = models.TextField()
    url = models.CharField(max_length=20)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    summary=models.TextField(max_length=1000)

def summary(self):
    return self.body[:100]

def __str__(self):
    return self.name    