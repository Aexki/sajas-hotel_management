from django.db import models

# Create your models here.
class roomservice(models.Model):
    name=models.CharField( max_length=50)
    service=models.CharField( max_length=50)
    completed=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class cabservice(models.Model):
    name=models.CharField( max_length=50)
    package=models.CharField(max_length=50)
    date=models.CharField( max_length=50)
    completed=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class complaintservice(models.Model):
    name=models.CharField( max_length=50)
    room=models.IntegerField()
    complaint=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name



