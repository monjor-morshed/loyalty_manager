from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.c_login, name='login'),
    path('dash/', views.dash, name='dash'),
    path('make_purchase/', views.make_purchase, name='make_purchase'),
    path('redeem_points/', views.redeem_points, name='redeem_points'),
    path('view_points/', views.view_points, name='view_points'),
    path('view_discount/', views.view_discount, name='view_discount'),
    path('logout/', views.c_logout, name='c_logout'),

]

