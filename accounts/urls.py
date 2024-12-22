from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.c_login, name='login'),
    path('success/', views.success, name='success'),  # Added path for success page
]

