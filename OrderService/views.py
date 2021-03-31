# from django.shortcuts import render, redirect
# from .models import OrderService
# from service.models import Category
# from registration.models import ServiceProvider, Customer
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout


# @login_required(login_url='/loginmodule/login')
# def show(request, user):
#     id = request.user.username
#     if user == 'cust':
#         orders = OrderService.objects.filter(c_id=id)
#         return render(request, 'CustShowOrder.html', {'orders': orders})
#     elif user == 'sp':
#         orders = OrderService.objects.filter(s_id=id)
#         return render(request, 'SpShowOrder.html', {'orders': orders, 'id': id})
#     else:
#         logout(request)
#         return redirect('/loginmodule/login')


# @login_required(login_url='/loginmodule/login')
# def delete(request, id):
#     order = OrderService.objects.get(id=id)
#     order.delete()
#     return redirect('/orderservice/show/cust')


# @login_required(login_url='/loginmodule/login')
# def add_order(request, id):
#     if request.method == 'POST':
#         city = request.POST.get('city', '')
#         mobile = request.POST.get('mobile', '')
#         address = request.POST.get('address', '')
#         email = request.POST.get('email', '')
#         s_id = id
#         c_id = request.user.username
#         order_status = "requested"
#         ob = OrderService()
#         ob.c_id = Customer.objects.get(username=c_id)
#         ob.s_id = ServiceProvider.objects.get(username=s_id)
#         ob.city = city
#         ob.mobile_no = mobile
#         ob.order_status = order_status
#         ob.address = address
#         ob.email = email
#         ob.save()
#         return redirect('/orderservice/show/cust')
#     else:
#         return render(request, 'OrderForm.html', {'id': id})


# def show_sp(request, category):
#     cat_ob = Category.objects.get(Category=category)
#     id = cat_ob.id
#     serviceProviders = ServiceProvider.objects.filter(cat_id=id)
#     return render(request, 'Show_sp.html', {'sps': serviceProviders})


# def update_status(request, id, status, type):
#     if type == 'sp':
#         order = OrderService.objects.get(id=id)
#         if status == 'done':
#             order.delete()
#         else:
#             order.order_status = status
#             order.save()
#         return redirect('/orderservice/show/sp')
#     elif type == 'cust':
#         order = OrderService.objects.get(id=id)
#         order.order_status = status
#         order.save()
#         return redirect('/orderservice/show/cust')
#     else:
#         msg = 'Invalid Access'
#         logout(request)
#         return redirect('/loginmodule/login')
from django.shortcuts import render, redirect
from .models import OrderService
from service.models import Category
from registration.models import ServiceProvider, Customer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required(login_url='/loginmodule/login')
def show(request, user):
    id = request.user.username
    if user == 'cust':
        orders = OrderService.objects.filter(c_id=id)
        return render(request, 'CustShowOrder.html', {'orders': orders})
    elif user == 'sp':
        orders = OrderService.objects.filter(s_id=id)
        return render(request, 'SpShowOrder.html', {'orders': orders, 'id': id})
    else:
        logout(request)
        return redirect('/loginmodule/login')


@login_required(login_url='/loginmodule/login')
def delete(request, id):
    order = OrderService.objects.get(id=id)
    order.delete()
    return redirect('/orderservice/show/cust')


@login_required(login_url='/loginmodule/login')
def add_order(request, id):
    if request.method == 'POST':
        city = request.POST.get('city', '')
        mobile = request.POST.get('mobile', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')
        s_id = id
        c_id = request.user.username
        order_status = "requested"
        ob = OrderService()
        ob.c_id = Customer.objects.get(username=c_id)
        ob.s_id = ServiceProvider.objects.get(username=s_id)
        ob.city = city
        ob.mobile_no = mobile
        ob.order_status = order_status
        ob.address = address
        ob.email = email
        ob.save()
        return redirect('/orderservice/show/cust')
    else:
        return render(request, 'OrderForm.html', {'id': id})


@login_required(login_url='/loginmodule/login')
def show_sp(request, category):
    cat_ob = Category.objects.get(Category=category)
    id = cat_ob.id
    serviceProviders = ServiceProvider.objects.filter(cat_id=id)
    return render(request, 'Show_sp.html', {'sps': serviceProviders})


@login_required(login_url='/loginmodule/login')
def update_status(request, id, status, type):
    if type == 'sp':
        order = OrderService.objects.get(id=id)
        if status == 'done':
            order.delete()
        else:
            order.order_status = status
            order.save()
        return redirect('/orderservice/show/sp')
    elif type == 'cust':
        order = OrderService.objects.get(id=id)
        order.order_status = status
        order.save()
        return redirect('/orderservice/show/cust')
    else:
        msg = 'Invalid Access'
        logout(request)
        return redirect('/loginmodule/login')
