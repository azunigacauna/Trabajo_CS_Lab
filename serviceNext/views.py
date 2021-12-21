from django.shortcuts import render, redirect
from usuarios.models import UsuarioProfesional, UsuarioNormal
from django.contrib.auth.models import User,auth
from distritos.models import Distrito
from profesiones.models import Profesion
from publicaciones.models import Publicacion
from profesiones.forms import profesionesForm
from publicaciones.forms import PublicacionForm

# Create your views here.
# Create your views here.
def index(request):
    profesiones = Profesion.objects.all()
    usuario=request.user.id
    if UsuarioNormal.objects.filter(UsuNorNomUsu_id=usuario).exists()==True:
        esNormal=True
    else:
        esNormal=False
    return render(request, "index.html",{'profesiones' : profesiones, 'esNormal': esNormal})

#vista para el link de login cliente
def loginCliente(request):
    return render(request, "login-Cliente.html")

#vista para el link de login cliente
def loginProfesional(request):
    return render(request, "login-Profesional.html")

def loginAdministrador(request):
    return render(request, "formAdmin.html")

def verPerfilUsuario(request):
    return render(request, "perfilUsuario.html")

#CRUD profesiones
def CRUDprofesiones(request):
    profesiones = Profesion.objects.all()
    return render(request, "CRUD_profesionales.html", {'profesiones' : profesiones})

def modificarProfesiones(request, id):
    profesiones = Profesion.objects.get(ProCod=id)
    if request.method == 'POST':
        form = profesionesForm(request.POST, request.FILES, instance=profesiones)
        if form.is_valid():
            eliminarProfesiones(request, id)
            form.save()
            return redirect('CRUDprofesiones')
    else:
        form = profesionesForm(instance=profesiones)
    return render(request, 'modificarProfesion.html', {
        'form': form
    })

def eliminarProfesiones(request, id):
    profesiones = Profesion.objects.get(ProCod=id)
    profesiones.delete()
    
    return redirect(to="CRUDprofesiones")

def agregarProfesiones(request):
    if request.method == 'POST':
        form = profesionesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('CRUDprofesiones')
    else:
        form = profesionesForm()
    return render(request, 'agregarProfesion.html', {
        'form': form
    })


#vista para las publicaciones de trabajo
def publicarTrabajo(request):
    if request.POST:
        publicacion = Publicacion()
        publicacion.Nombres = request.POST.get('Nombres')
        publicacion.Apellidos = request.POST.get('Apellidos')       
        publicacion.Correo = request.POST.get('Correo')
        publicacion.Distrito= request.POST.get('Distrito')
        publicacion.Descripcion = request.POST.get('Descripcion')
        publicacion.Celular = request.POST.get('Celular')
        publicacion.EstadoTrabajo = request.POST.get('EstadoTrabajo')
        publicacion.save()
        return redirect('registroExitoso')
    return render (request, 'publicar.html') 

def registroExitoso(request):
    return render(request, "exitosa.html")


def modificarTrabajo(request, id):
    propuestas = Publicacion.objects.get(id=id)
    if request.method == 'POST':
        form = PublicacionForm(request.POST, instance=propuestas)
        if form.is_valid():
            form.save()
            
            return redirect('registroExitoso')
    else:
        form = PublicacionForm(instance=propuestas)
    return render(request, 'publicar2.html', {
        'form': form
    })

#Calificacion de profesional
def calificacion(request):
    profesionales = UsuarioProfesional.objects.all()
    return render(request, "calificacionProfesional.html", {'profesionales' : profesionales})
    #return render(request, "calificacionProfesional.html")

# Responder oferta de trabajo
def responderOferta(request):
    return render(request, "responder.html")

def perfilProfesional(request):
    usuario=request.user.id
    print(usuario)
    nombre=User.objects.get(id__exact=usuario)#sacado de la tabla users
    nombre2=UsuarioProfesional.objects.get(UsuProNomUsu_id__exact=usuario)#sacado de profesionales
    direccioncod=nombre2.UsuProDisCod_id
    direccion=Distrito.objects.get(DisCod__exact=direccioncod)
    if request.method == 'POST':
        if request.POST.get('primero')=="first":
            valo=1
        elif request.POST.get('segundo')=="second":
            valo=2
        elif request.POST.get('tercero')=="third":
            valo=3
        elif request.POST.get('cuarto')=="fourth":
            valo=4
        elif request.POST.get('quinto')=="fifth":
            valo=5
        print("Se pudo entrar lets go\n")
        obj=UsuarioProfesional.objects.get(UsuProNomUsu_id__exact=usuario)
        if obj.UsuProPun==0 and obj.UsuProCal==0:
            obj.UsuProPun=1
            obj.UsuProCal=1
            obj.save()
        print(valo)
        puntuaciones=obj.UsuProPun
        obj.UsuProPun=obj.UsuProPun+1
        valorantiguo=obj.UsuProCal
        encx=puntuaciones*valorantiguo
        obj.UsuProCal=(encx+valo)/obj.UsuProPun
        obj.save()
    return render(request, "perfilProfesional.html", {"nombre": nombre, "nombre2": nombre2, "direccion": direccion})

def perfilUsuario(request):
    usuario=request.user.id
    print(usuario)
    nombre=User.objects.get(id__exact=usuario)#sacado de la tabla users
    nombre2=UsuarioNormal.objects.get(UsuNorNomUsu_id__exact=usuario)#sacado de usuariosnormales
    direccioncod=nombre2.UsuNorDisCod_id
    direccion=Distrito.objects.get(DisCod__exact=direccioncod)
    return render(request, "perfilUsuario.html", {"nombre": nombre, "nombre2":nombre2, "direccion": direccion})



#CRUD profesiones

# def verOfertasProfesional(request):
#     return render(request,"ofertasProfesional.html")

# def responderOfertaProfesional(request):
#     return render(request,"responder.html")