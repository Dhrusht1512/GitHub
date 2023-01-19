from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def base(request):
    return render(request, 'main_app/base.html')


def log(request):
    return render(request, 'login.html')


def forgot(request):
    return render(request, 'forgotpassword.html')


def success(request):
    return render(request, 'main_app/index.html')
