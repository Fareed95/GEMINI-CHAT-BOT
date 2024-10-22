from django.db import models

from django.contrib.auth.models import User

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    image = models.ImageField(upload_to ='uploads/',null=True, blank = True) 
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
