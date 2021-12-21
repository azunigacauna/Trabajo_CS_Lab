from django.shortcuts import redirect, render
from django.contrib import messages #para que se realice correctamente el mensaje
from django.contrib.auth.models import User, auth

from usuarios.models import UsuarioNormal, UsuarioProfesional
# Create your views here.

def registroCliente(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #Verifica la primera contraseña y la segunda de autenticidad
        if password1 == password2:
            #Verifica la existencia del usuario en la BD
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Taken")
                return redirect("registroCliente")
            elif User.objects.filter(email = email).exists():
                messages.info(request,"E-mail Taken")
                return redirect("registroCliente")
            else:
                user = User.objects.create_user(username = username, password = password1, email = email,
                first_name = first_name, last_name = last_name)
                usuarioN = UsuarioNormal.objects.create(UsuNorNomUsu = user)
                user.save();
                usuarioN.save();
                print("User Created")
                return redirect("loginCliente")

        else:
            messages.info(request,"Password not Maching...")
            return redirect("registroCliente")
        return redirect("/")

    else:
        return render(request,"login-Cliente.html")

# Create your views here.
def loginCliente(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("loginCliente")
    else:
        return render(request,"login-Cliente.html")


def logoutCliente(request):
    auth.logout(request)
    return redirect("/")



# PARA EL CASO DE PROFESIONAL TENDREMOS LAS SIGUIENTES ACCIONES DE REGISTRO, LOGIN Y LOGOUT
def registroProfesional(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        is_staff = 1

        #Verifica la primera contraseña y la segunda de autenticidad
        if password1 == password2:
            #Verifica la existencia del usuario en la BD
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Taken")
                return redirect("registroProfesional")
            elif User.objects.filter(email = email).exists():
                messages.info(request,"E-mail Taken")
                return redirect("registroProfesional")
            else:
                user = User.objects.create_user(username = username, password = password1, email = email,
                first_name = first_name, last_name = last_name, is_staff = 1)
                profesional = UsuarioProfesional.objects.create(UsuProNomUsu = user)
                user.save();
                profesional.save();
                print("User Created")
                return redirect("loginProfesional")

        else:
            messages.info(request,"Password not Maching...")
            return redirect("registroProfesional")
        return redirect("/")

    else:
        return render(request,"login-Profesional.html")

# Create your views here.
def loginProfesional(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("loginProfesional")
    else:
        return render(request,"login-Profesional.html")


def logoutProfesional(request):
    auth.logout(request)
    return redirect("/")


##########PARA EL ADMINISTRADOR

def loginAdministrador(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("CRUDprofesiones")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("loginAdministrador")
    else:
        return render(request,"formAdmin.html")

def logoutAdministrador(request):
    auth.logout(request)
    return redirect("/")