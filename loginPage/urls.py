from django.urls import path
from . import views

urlpatterns = [
    path('loginsuccess/', views.success),
    path('forgotpassword/', views.forgot),
    path('', views.log)
]