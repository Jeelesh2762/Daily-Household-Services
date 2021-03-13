# from django.urls import path
# from loginmodule.views import about, home, admin_view, login, auth_view, logout, register, customer_view, service_provider_view
# from django.contrib.auth import views as auth_views
# from django.conf.urls import url
# from . import views
# urlpatterns = [
#     url(r'^login/$', login),
#     url(r'^auth/$', auth_view),
#     url(r'^logout/$', logout),
#     url(r'^register/$', register),
#     path('customer', customer_view),
#     path('serviceprovider', service_provider_view),
#     path('admin', admin_view),
#     path('home', home),
#     path('about', about)
# ]
from django.urls import path
from loginmodule.views import about, home, admin_view, login, auth_view, logout, customer_view, service_provider_view
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login/$', login),
    url(r'^auth/$', auth_view),
    url(r'^logout/$', logout),
    path('customer', customer_view),
    path('serviceprovider', service_provider_view),
    path('admin', admin_view),
    path('home', home),
    path('about', about),
]
