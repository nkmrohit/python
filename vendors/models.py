from django.db import models

# Create your models here.
class vendors(models.Model):
    #company fields
    c_name = models.CharField(max_length=20)
    c_owner = models.CharField(max_length=20)
    c_reg_no = models.IntegerField()
    c_adress = models.TextField(max_length=20)
    c_phone  = models.IntegerField()
    c_email = models.EmailField(max_length=20)
    c_description = models.TextField(max_length=200)
    c_url= models.URLField(max_length=50, default='NULL')
    c_logo = models.ImageField(upload_to='images/', default='NULL')
    c_created_date = models.DateTimeField()
    c_updated_date = models.DateTimeField()
    #user fields
    firstname= models.CharField(max_length=20)
    lastname= models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    image = models.ImageField(upload_to='images/', default="NULL")
    username= models.CharField(max_length=20)
    password= models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)

def __str__(self):
    return self.c_name  
