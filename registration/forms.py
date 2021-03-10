from django import forms
from .models import Customer, ServiceProvider
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


class CustomerForm(forms.ModelForm):
    address = forms.CharField(required=False)
    mobile_no = forms.CharField(required=False)
    username = forms.CharField(required=False)
    city = forms.CharField(required=False)

    class Meta:
        model = Customer
        fields = ['username', 'password', 'first_name',
                  'last_name', 'address', 'email', 'mobile_no', 'city']


class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = ['username', 'password', 'first_name', 'last_name', 'address', 'email',
                  'mobile_no', 'city', 'cat_id', 'service_rate', 's_license', 'profile_description']
