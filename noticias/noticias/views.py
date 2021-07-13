from django.http import HttpResponse 
def saludo (request):
    return HttpResponse("hola como estas me llamo camilo")