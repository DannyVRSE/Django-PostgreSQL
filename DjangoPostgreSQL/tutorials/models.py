from django.db import models

# Create your models here.
#Create table called 'Tutorials'
#id is added automatically
class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)