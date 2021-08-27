#librerias de python
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.core.paginator import Paginator

#librerias mias
from .forms import *
from .models import *
from .admin import *

def home(request):
    context={}
    return render(request, 'index.html', context)


def pagina_registro(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='participante')
            user.groups.add(group)
            participante.objects.create(user=user,nombre=user.username,email=user.email)
            messages.success(request, 'la carga ha sido exitosa ' + username)
            return redirect('login')



    context={'form': form}
    return render(request,'registro.html',context)



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'el usuario o la contra, son invalidos')
            
    context ={}

    return render(request,'login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def inicio_juego(request):
    context = {}
    return render(request, 'inicio_juego.html',context)


def Usuario(request):
    Usuarios = User.objects.all()
    usuarios_totales = User.objects.count()
    admin= Usuarios.filter(is_superuser=True).count()
    participante= Usuarios.filter(is_superuser=False).count()
    paginator = Paginator(Usuarios,4)
    page= request.GET.get('page')
    Usuarios = paginator.get_page(page)
    context ={'participantes':Usuarios, 'usuarios_totales':usuarios_totales, 'admin':admin, 'participante':participante}

    return render(request,'usuarios.html',context)
