# from django.shortcuts import render
# from django.views.generic import TemplateView
# from django.http import HttpResponseRedirect
# from django.contrib import auth
# from django.template.context_processors import csrf
# from django.contrib.auth.decorators import login_required
# from registration.models import Customer, ServiceProvider

# # Create your views here.


# def login(request):
#     c = {}
#     c.update(csrf(request))
#     return render(None, 'login.html', c)


# def auth_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user_type = request.POST.get('user_type', '')
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             # auth.login(request, user)
#             if user_type == 'cust':
#                 # this is also demo page,design it
#                 # return HttpResponseRedirect('/loginmodule/customer')
#                 try:
#                     user1 = Customer.objects.get(username=username)
#                 except:
#                     msg = "Wrong Username or Password"
#                     return render(request, 'login.html', {'msg': msg})
#                 else:
#                     auth.login(request, user)
#                     return HttpResponseRedirect('/loginmodule/customer')

#             elif user_type == 'sp':
#                 # it's only demo page you have to design it
#                 # return HttpResponseRedirect('/loginmodule/serviceprovider')
#                 try:
#                     user1 = ServiceProvider.objects.get(username=username)
#                 except:
#                     auth.login(request, user)
#                     msg = "Wrong Username or Password!"
#                     return render(request, 'login.html', {'msg': msg})
#                 else:
#                     auth.login(request, user)
#                     return HttpResponseRedirect('/loginmodule/serviceprovider')
#             elif user.is_superuser == 1:
#                 # redirect him to admin page
#                 auth.login(request, user)
#                 return HttpResponseRedirect('/loginmodule/admin')
#         else:
#             msg = "Wrong Username or Password"
#             return render(request, 'login.html', {'msg': msg})


# # def loggedin(request):
# #     return render(None, 'loggedin.html', {"full_name": request.user.username})


# # def invalidlogin(request):
# #     return render(None, 'invalidlogin.html')


# def logout(request):
#     auth.logout(request)
#     return render(None, 'logout.html')


# def register(request):
#     return render(None, 'register.html')


# @login_required(login_url='/loginmodule/login/')
# def customer_view(request):
#     username = request.user.username
#     try:
#         user1 = Customer.objects.get(username=username)
#     except:
#         msg = "Invalid Access"
#         return render(request, 'login.html', {'msg': msg})
#     else:
#         return render(request, 'customer.html', {'name': request.user.username})


# @login_required(login_url='/loginmodule/login/')
# def service_provider_view(request):
#     username = request.user.username
#     try:
#         user1 = ServiceProvider.objects.get(username=username)
#     except:
#         msg = "Invalid Access"
#         return render(request, 'login.html', {'msg': msg})
#     else:
#         return render(request, 'serviceprovider.html')


# @login_required(login_url='/loginmodule/login/')
# def admin_view(request):
#     if request.user.is_superuser:
#         return render(request, 'admin.html')
#     else:
#         auth.logout(request)
#         return redirect('/loginmodule/login')


# @login_required(login_url='/loginmodule/login/')
# def home(request):
#     return render(None, 'home.html')


# def about(request):
#     return render(None, 'about.html')
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from registration.models import Customer, ServiceProvider

# Create your views here.


def login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'login.html', c)


def auth_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user_type = request.POST.get('user_type', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user_type == 'cust':
                try:
                    user1 = Customer.objects.get(username=username)
                except:
                    msg = "Wrong Username or Password"
                    return render(request, 'login.html', {'msg': msg})
                else:
                    auth.login(request, user)
                    return HttpResponseRedirect('/loginmodule/customer')
            elif user_type == 'sp':
                try:
                    user1 = ServiceProvider.objects.get(username=username)
                except:
                    auth.login(request, user)
                    msg = "Wrong Username or Password"
                    return render(request, 'login.html', {'msg': msg})
                else:
                    auth.login(request, user)
                    return HttpResponseRedirect('/loginmodule/serviceprovider')
            elif user.is_superuser == 1:
                auth.login(request, user)
                return HttpResponseRedirect('/loginmodule/admin')
        else:
            msg = "Wrong Username or Password"
            return render(request, 'login.html', {'msg': msg})


@login_required(login_url='/loginmodule/login/')
def logout(request):
    auth.logout(request)
    return render(request, 'home.html')


@login_required(login_url='/loginmodule/login/')
def customer_view(request):
    username = request.user.username
    try:
        user1 = Customer.objects.get(username=username)
    except:
        msg = "Invalid Access"
        return render(request, 'login.html', {'msg': msg})
    else:
        return render(request, 'customer.html', {'name': request.user.username})


@login_required(login_url='/loginmodule/login/')
def service_provider_view(request):
    username = request.user.username
    try:
        user1 = ServiceProvider.objects.get(username=username)
    except:
        msg = "Invalid Access"
        return render(request, 'login.html', {'msg': msg})
    else:
        return render(request, 'serviceprovider.html', {'name': username})


@login_required(login_url='/loginmodule/login/')
def admin_view(request):
    if request.user.is_superuser:
        return render(request, 'admin.html')
    else:
        auth.logout(request)
        return redirect('/loginmodule/login')


def home(request):
    return render(request, 'home.html')


def about(request):
    is_active = False
    user_type = ""
    username = request.user.username
    if username != "":
        is_active = True
        try:
            user1 = Customer.objects.get(username=username)
            user_type = "cust"
        except:
            pass
        try:
            user1 = ServiceProvider.objects.get(username=username)
            user_type = "sp"
        except:
            pass
    return render(request, 'about.html', {'is_active': is_active, 'user_type': user_type})
