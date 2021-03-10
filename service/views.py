from django.shortcuts import render, redirect
from .models import Category
from .form import ServiceForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/loginmodule/login/')
def add_service(request):
    if request.method == "POST":
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
        form = ServiceForm()
        return render(request, 'AddService.html', {'form': form})


@login_required(login_url='/loginmodule/login/')
def show(request):
    services = Category.objects.all()
    return render(request, 'ShowService.html', {'services': services})


@login_required(login_url='/loginmodule/login/')
def delete(request, id):
    service = Category.objects.get(id=id)
    service.delete()
    return redirect('/service/show')
