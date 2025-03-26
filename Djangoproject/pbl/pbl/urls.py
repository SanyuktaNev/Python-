from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('home/', views.home),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.Register.as_view(), name='register'),
]
