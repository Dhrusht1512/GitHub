from django.contrib import admin
from django.urls import path, include
from SystemApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.log_in, name='log_in'),
    path('do_login/', views.do_login, name='do_login'),
    path('base', views.base, name='base'),
    path('add_student', views.add_student, name='add_student')
]
