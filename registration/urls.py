from django.contrib import admin  
from django.urls import path  
from . import views  
urlpatterns = [   
    path('CustomerSignup', views.CustomerSignup),  
    path('SpSignup',views.SpSignup),  
    path('signup',views.signup),  
]  