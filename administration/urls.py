from django.urls import path
from . import views


urlpatterns = [
    path('show/<str:type>', views.show),
    path('delete/<str:type>,<str:id>', views.delete),
]
