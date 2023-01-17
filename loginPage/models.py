from django.db import models

# Create your models here.
class students_login_credentials(models.Model):
    username = models.CharField(max_length=50, unique=True, null=False, primary_key=True)
    password = models.CharField(max_length=20, unique=True, null=False)

class faculty_login_credentials(models.Model):
    username = models.CharField(max_length=50, unique=True, null=False, primary_key=True)
    password = models.CharField(max_length=20, unique=True, null=False)
    
class admin_or_hod_login_credentials(models.Model):
    username = models.CharField(max_length=50, unique=True, null=False, primary_key=True)
    password = models.CharField(max_length=20, unique=True, null=False)