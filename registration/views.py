# from django.shortcuts import render, redirect
# from .forms import CustomerForm, ServiceProviderForm
# from django.contrib.auth.models import User
# from django.contrib import messages

# # Create your views here.


# def CustomerSignup(request):
#     form = CustomerForm(request.POST)
#     if form.is_valid():
#         try:
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             email = form.cleaned_data.get('email')
#             fname = form.cleaned_data.get('first_name')
#             lname = form.cleaned_data.get('last_name')
#             user = User.objects.create_user(username, email, password)
#             user.first_name = fname
#             user.last_name = lname
#             user.save()
#             form.save()
#             return redirect("/loginmodule/login")
#         except Exception:
#             msg = "This user name has been taken."
#             return render(request=request, template_name='cust_registration.html', context={'form': form, 'msg': msg})
#     else:
#         return render(request=request,template_name='cust_registration.html',context={'form':form})

# def SpSignup(request):
#     form = ServiceProviderForm(request.POST)
#     if form.is_valid():
#         try:
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             email = form.cleaned_data.get('email')
#             fname = form.cleaned_data.get('first_name')
#             lname = form.cleaned_data.get('last_name')
#             user = User.objects.create_user(username,email,password)
#             user.first_name = fname
#             user.last_name = lname
#             user.save()
#             form.save()
#             return redirect("/loginmodule/login")
#         except Exception :
#             msg = "This user name has been taken."
#             return render(request=request,template_name='sp_registration.html',context={'form':form,'msg':msg})
#     else:
#         return render(request=request,template_name='sp_registration.html',context={'form':form})

# def signup(request):
#     return render(None, 'reg_home.html')

from django.shortcuts import render, redirect
from .forms import CustomerForm, ServiceProviderForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def CustomerSignup(request):
    form = CustomerForm(request.POST)
    if form.is_valid():
        try:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            form.save()
            return redirect("/loginmodule/login")
        except Exception:
            msg = "This user name has been taken."
            return render(request=request, template_name='cust_registration.html', context={'form': form, 'msg': msg})
    else:
        return render(request=request, template_name='cust_registration.html', context={'form': form})


def SpSignup(request):
    form = ServiceProviderForm(request.POST)
    if form.is_valid():
        try:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            fname = form.cleaned_data.get('first_name')
            lname = form.cleaned_data.get('last_name')
            user = User.objects.create_user(username, email, password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            form.save()
            return redirect("/loginmodule/login")
        except Exception:
            msg = "This user name has been taken."
            return render(request=request, template_name='sp_registration.html', context={'form': form, 'msg': msg})
    else:
        return render(request=request, template_name='sp_registration.html', context={'form': form})


def signup(request):
    return render(request, 'reg_home.html')
