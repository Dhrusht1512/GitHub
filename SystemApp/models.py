from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    USER = [
        (1, 'HOD'),
        (2, 'Faculty'),
        (3, 'STUDENT'),
    ]

    user_type = models.CharField(choices=USER, max_length=50)
    profile_pic = models.ImageField(upload_to='media/profile_pic', blank=True)

# class students_login_credentials(models.Model):
#     username = models.CharField(
#         max_length=255, unique=True, null=False, primary_key=True)
#     password = models.CharField(max_length=20, unique=True, null=False)


# class faculty_login_credentials(models.Model):
#     username = models.CharField(
#         max_length=255, unique=True, null=False, primary_key=True)
#     password = models.CharField(max_length=20, unique=True, null=False)


# class admin_or_hod_login_credentials(models.Model):
#     username = models.CharField(
#         max_length=255, unique=True, null=False, primary_key=True)
#     password = models.CharField(max_length=20, unique=True, null=False)
