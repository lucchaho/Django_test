from django.db import models

# Create your models here.

class User_ayomi(models.Model):
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.email