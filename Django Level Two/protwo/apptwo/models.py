from django.db import models

# Create your models here.

class users(models.Model):
    first_name= models.CharField(max_length=124)
    last_name= models.CharField(max_length=124)
    email=models.EmailField(max_length=224,unique=True)
    