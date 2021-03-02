from django.db import models


class UserDetails(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    consent = models.IntegerField()





