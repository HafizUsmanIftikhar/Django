from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name= models.CharField(max_length=256)

    def __str__(self):
        return self.top_name
    
class Webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=244,unique=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name= models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateTimeField()

    def __str__(self):
        return str(self.date)
