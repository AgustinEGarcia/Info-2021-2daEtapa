from django.shortcuts import render

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