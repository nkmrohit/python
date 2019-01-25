from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.
class Customers(models.Model):
    """Model definition for MODELNAME."""
    fname = models.CharField(max_length=15)
    mname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    phone = models.PositiveIntegerField()
    email = models.EmailField(max_length=254, blank=False, unique=True, validators=[validate_email])
    address = models.TextField()
    image = models.ImageField(upload_to='images/')
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.fname+' '+self.mname+' '+self.lname
