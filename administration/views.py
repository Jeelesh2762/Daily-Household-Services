# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import logout
# from registration.models import Customer, ServiceProvider
# from django.contrib.auth.decorators import login_required


# @login_required(login_url='/loginmodule/login')
# def show(request, type):
#     if request.user.is_superuser:
#         if type == 'cust':
#             customers = Customer.objects.all()
#             return render(request, 'ShowCustomers.html', {'customers': customers})
#         elif type == 'sp':
#             service_providers = ServiceProvider.objects.all()
#             return render(request, 'ShowServiceProviders.html', {'sps': service_providers})
#         else:
#             msg = 'Invalid Access'
#             logout(request)
#             return render(request, 'login.html', {'msg': msg})
#     else:
#         msg = 'Invalid Access'
#         logout(request)
#         return render(request, 'login.html', {'msg': msg})


# @login_required(login_url='/loginmodule/login')
# def delete(request, type, id):
#     if request.user.is_superuser:
#         user = User.objects.get(username=id)
#         user.delete()
#         if type == 'cust':
#             cust_user = Customer.objects.get(username=id)
#             cust_user.delete()
#             return redirect('/administration/show/cust')
#         elif type == 'sp':
#             sp_user = ServiceProvider.objects.get(username=id)
#             sp_user.delete()
#             return redirect('/administration/show/sp')
#         else:
#             msg = 'Invalid Access'
#             logout(request)
#             return render(request, 'login.html', {'msg': msg})
#     else:
#         msg = 'Invalid Access'
#         logout(request)
#         return render(request, 'login.html', {'msg': msg})
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from registration.models import Customer, ServiceProvider
from django.contrib.auth.decorators import login_required


@login_required(login_url='/loginmodule/login')
def show(request, type):
    if request.user.is_superuser:
        if type == 'cust':
            customers = Customer.objects.all()
            return render(request, 'ShowCustomers.html', {'customers': customers})
        elif type == 'sp':
            service_providers = ServiceProvider.objects.all()
            return render(request, 'ShowServiceProviders.html', {'sps': service_providers})
        else:
            msg = 'Invalid Access'
            logout(request)
            return render(request, 'login.html', {'msg': msg})
    else:
        msg = 'Invalid Access'
        logout(request)
        return render(request, 'login.html', {'msg': msg})


@login_required(login_url='/loginmodule/login')
def delete(request, type, id):
    if request.user.is_superuser:
        user = User.objects.get(username=id)
        user.delete()
        if type == 'cust':
            cust_user = Customer.objects.get(username=id)
            cust_user.delete()
            return redirect('/administration/show/cust')
        elif type == 'sp':
            sp_user = ServiceProvider.objects.get(username=id)
            sp_user.delete()
            return redirect('/administration/show/sp')
        else:
            msg = 'Invalid Access'
            logout(request)
            return render(request, 'login.html', {'msg': msg})
    else:
        msg = 'Invalid Access'
        logout(request)
        return render(request, 'login.html', {'msg': msg})
