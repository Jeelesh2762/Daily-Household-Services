from django.urls import path
from . import views

urlpatterns = [
    # path('home',views.home),
    path('add/<str:id>', views.add_order),
    path('delete/<int:id>', views.delete),
    path('show/<str:user>', views.show),
    path('show_sp/<str:category>', views.show_sp),
    path('update_status/<int:id>,<str:status>,<str:type>', views.update_status),
]
