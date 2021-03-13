from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_service),
    path('show', views.show),
    path('delete/<int:id>', views.delete),
    path('services', views.services)
]
