from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginPage/', include('loginPage.urls')),
    path('forgotpassword/', include('loginPage.urls')),
    path('loginsuccess/', include('loginPage.urls')),
    path('', include('loginPage.urls')),
]
