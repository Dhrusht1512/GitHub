from django.urls import path
from . import views

urlpatterns = [
    path('forgotpassword/', views.forgot),
    path('', views.log)
]