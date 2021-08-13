from django.db import models

class login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)
    password_confirmation = models.CharField(max_length=30)