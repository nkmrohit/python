from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
        """ an actual singular human being """
        name = models.CharField(blank=True, max_length=100)
        email = models.EmailField()
        created_at = models.DateTimeField(auto_now=True)
        #created_by = models.ForeignKey(User, blank=True, null=True)
        created_by = models.ForeignKey(User,on_delete=models.CASCADE)

        def __unicode__(self):
                return self.name