from django.db import models

class User(models.Model):
    objects = None
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email_id = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
