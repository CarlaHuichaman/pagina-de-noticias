from django.shortcuts import render , redirect , get_object_or_404
from .models import Categoria , Periodista , Noticia
from .forms import ContactoForm , NoticiaForm
from django.contrib import messages
# Create your views here.


def index(request):
    noticia = Noticia.objects.all()
    datos={
        'noticias': noticia
    }
    return render(request,'core/index.html', datos)

def buscadornoticias(request):
    return render(request,'core/buscadornoticias.html')


def contacto(request):
    data={
        'form':ContactoForm()
    }

    if request.method =='POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="contacto guardado"
        else:
            data["form"]=formulario
    return render(request,'core/contacto.html',data)

def detallenoticia(request):
    noticia = Noticia.objects.filter(categoria=3)
    datos={
        'noticias': noticia
    }
    return render(request,'core/detallenoticia.html',datos)

def datoutil(request):
    return render(request,'core/datoutil.html')

def galeriadefotos(request):
    return render(request,'core/galeriadefotos.html')

def login(request):
    return render(request,'core/login.html')

def mundo(request):
    noticia = Noticia.objects.filter(categoria=1)
    datos={
        'noticias': noticia
    }
    return render(request,'core/mundo.html',datos)

def nacional(request):
    noticia = Noticia.objects.filter(categoria=2)
    datos={
        'noticias': noticia
    }
    return render(request,'core/nacional.html',datos)

def nosotros(request):
    return render(request,'core/nosotros.html')

def pagperiodista(request):
    return render(request,'core/pagperiodista.html')

def registro(request):
    return render(request,'core/registro.html')

def datoutil1(request):
    return render(request,'core/datoutil1.html')

def datoutil2(request):
    return render(request,'core/datoutil2.html')

def mundo1(request):
    return render(request,'core/mundo1.html')

def mundo2(request):
    return render(request,'core/mundo2.html')

def nacional1(request):
    return render(request,'core/nacional1.html')

def nacional2(request):
    return render(request,'core/nacional2.html')

def periodista1(request):
    return render(request,'core/periodista1.html')

def periodista2(request):
    return render(request,'core/periodista2.html')

def periodista3(request):
    return render(request,'core/periodista3.html')

def periodista4(request):
    return render(request,'core/periodista4.html')

def periodista5(request):
    return render(request,'core/periodista5.html')

def periodista6(request):
    return render(request,'core/periodista6.html')

def agregar_noticia(request):
    data={
        'form':NoticiaForm()
    }
    if request.method =='POST':
        formulario = NoticiaForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Noticia registrada")
        else:
            data["form"]=formulario
    return render(request,'core/noticia/agregar.html',data)

def listar_noticia(request):
    noticias= Noticia.objects.all()
    data={
        'noticias':noticias
    }
    return render(request,'core/noticia/listar.html',data)

def modificar_noticia(request,id):
    noticia=get_object_or_404(Noticia,id=id)
    data={
        'form':NoticiaForm(instance=noticia)
    }
    if request.method=='POST':
        formulario=NoticiaForm(data=request.POST,instance=noticia, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"modificado correctamente")
            return redirect(to="listar_noticia")
        data["form"]=formulario
    return render(request,'core/noticia/modificar.html',data)

def eliminar_noticia(request,id):
    noticia=get_object_or_404(Noticia,id=id)
    noticia.delete()
    messages.success(request,"eliminado correctamente")
    return redirect(to="listar_noticia")