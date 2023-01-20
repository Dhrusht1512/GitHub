from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(models.Model):
    USER_TYPE = [
        (1, 'HOD'),
        (2, 'Staff'),
        (3, 'Student')
    ]
    user_type = models.CharField(max_length=255, choices=USER_TYPE)
    profile_pic = models.FileField(upload_to='media/profile_pic')


class students_login_credentials(models.Model):
    username = models.CharField(
        max_length=255, unique=True, null=False, primary_key=True)
    password = models.CharField(max_length=20, unique=True, null=False)


class faculty_login_credentials(models.Model):
    username = models.CharField(
        max_length=255, unique=True, null=False, primary_key=True)
    password = models.CharField(max_length=20, unique=True, null=False)


class admin_or_hod_login_credentials(models.Model):
    username = models.CharField(
        max_length=255, unique=True, null=False, primary_key=True)
    password = models.CharField(max_length=20, unique=True, null=False)
