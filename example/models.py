
from django.db import models

class UserDataModel(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    
    identifier = models.CharField(max_length=300, default="")
    
    def __str__(self):
        return self.username
    
class UserBlogModel(models.Model):
    username = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    image = models.FileField(default="___")
    
    numOfTrashPickedUp = models.IntegerField(default=0)
    numOfPPl = models.IntegerField(default=0)
    isPicturePublic = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.username} - {self.content[:20]}..."