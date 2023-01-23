from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from SystemApp.EmailBackEnd import EmailBackEnd
from django.contrib import messages
from .models import CustomUser
# Create your views here.


def log_in(request):
    return render(request, 'main_app/login.html')


def do_login(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request, username=request.POST.get(
            'username'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('base')
            elif user_type == '2':
                return HttpResponse('This is Faculty page.')
            elif user_type == '3':
                return HttpResponse('This is Staff page.')
            else:
                messages.error(request, 'Username and Password are Invalid !')
                return redirect('log_in')
        else:
            messages.error(request, 'Email and Password Are Invalid !')
            return redirect('log_in')


def base(request):
    return render(request, 'main_app/base.html')


def add_student(request):
    return render(request, 'hod_template/add_student_template.html')
