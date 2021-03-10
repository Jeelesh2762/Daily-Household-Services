from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
    c = {}
    c.update(csrf(request))
    return render(None, 'login.html', c)


def auth_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user_type = request.POST.get('user_type', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if user_type == 'cust':
                # this is also demo page,design it
                return HttpResponseRedirect('/loginmodule/customer')
            elif user_type == 'sp':
                # it's only demo page you have to design it
                return HttpResponseRedirect('/loginmodule/serviceprovider')
            elif user.is_superuser == 1:
                # redirect him to admin page
                return HttpResponseRedirect('/loginmodule/admin')
            else:
                msg = "Wrong UserType"
                return render(request, 'login.html', {'msg': msg})
        else:
            msg = "Wrong Username or Password"
            return render(request, 'login.html', {'msg': msg})


def loggedin(request):
    return render(None, 'loggedin.html', {"full_name": request.user.username})


def invalidlogin(request):
    return render(None, 'invalidlogin.html')


def logout(request):
    auth.logout(request)
    return render(None, 'logout.html')


def register(request):
    return render(None, 'register.html')


@login_required(login_url='/loginmodule/login/')
def customer_view(request):
    return render(None, 'customer.html', {'name': request.user.username})


@login_required(login_url='/loginmodule/login/')
def service_provider_view(request):
    return render(None, 'serviceprovider.html')

@login_required(login_url='/loginmodule/login/')
def admin_view(request):
    return render(None, 'admin.html')


@login_required(login_url='/loginmodule/login/')
def home(request):
    return render(None, 'home.html')


def about(request):
    return render(None, 'about.html')
