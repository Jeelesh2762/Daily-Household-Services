# from django.shortcuts import render, redirect
# from .models import Category
# from .form import ServiceForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout


# @login_required(login_url='/loginmodule/login')
# def add_service(request):
#     if request.method == "POST":
#         if request.user.is_superuser:
#             try:
#                 form = ServiceForm(request.POST)
#                 if form.is_valid():
#                     form.save()
#                     return redirect('/service/show')
#                 else:
#                     raise FormError("not valid form")
#             except FormError:
#                 render(request, 'error.html')
#         else:
#             logout(request)
#             return redirect('/loginmodule/login')
#     else:
#         form = ServiceForm()
#         return render(request, 'AddService.html', {'form': form})


# @login_required(login_url='/loginmodule/login')
# def show(request):
#     if request.user.is_superuser:
#         services = Category.objects.all()
#         return render(request, 'ShowService.html', {'services': services})
#     else:
#         logout(request)
#         return redirect('/loginmodule/login')


# @login_required(login_url='/loginmodule/login')
# def delete(request, id):
#     if request.user.is_superuser:
#         service = Category.objects.get(id=id)
#         service.delete()
#         return redirect('/service/show')
#     else:
#         logout(request)
#         return redirect('/loginmodule/login')
from django.shortcuts import render, redirect
from .models import Category
from .form import ServiceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required(login_url='/loginmodule/login')
def add_service(request):
    if request.method == "POST":
        if request.user.is_superuser:
            try:
                form = ServiceForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('/service/show')
                else:
                    raise FormError("not valid form")
            except FormError:
                render(request, 'error.html')
        else:
            logout(request)
            return redirect('/loginmodule/login')
    else:
        form = ServiceForm()
        return render(request, 'AddService.html', {'form': form})


@login_required(login_url='/loginmodule/login')
def show(request):
    if request.user.is_superuser:
        services = Category.objects.all()
        return render(request, 'ShowService.html', {'services': services})
    else:
        logout(request)
        return redirect('/loginmodule/login')


@login_required(login_url='/loginmodule/login')
def delete(request, id):
    if request.user.is_superuser:
        service = Category.objects.get(id=id)
        service.delete()
        return redirect('/service/show')
    else:
        logout(request)
        return redirect('/loginmodule/login')


@login_required(login_url='/loginmodule/login')
def services(request):
    return render(request, 'Services.html')
