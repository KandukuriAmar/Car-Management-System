from django.urls import path
from .views import *

urlpatterns=[
    path('',navbar,name='navbar'),
    path('home/',home,name="home"),
    path('login/',login,name='login'),
    path('register/',signup,name='registercall'),
    path('registerlogin/',registerlogin,name='registerlogin'),
    path('carbook/',carbook,name='carbook'),
    path('takerentcar/',takerentcar,name='takerentcar'),
    path('login1',login1,name='login1'),
    path('logout/', logout, name='logout'),
    path('car1/',car1,name='car1'),
    path('car2/',car2,name='car2'),
    path('car/',car,name='car'),
    path('car3/',car3,name='car3'),
    path('car4/',car4,name='car4'),
    path('car5/',car5,name='car5'),
    path('car6/',car6,name='car6'),
    path('car7/',car7,name='car7'),
    path('car8/',car8,name='car8'),
    path('car9/',car9,name='car9'),
    path('car10/',car10,name='car10'),
    path('book/',book,name='book'),

]