from django.contrib import admin
from .models import Categoria , Periodista , Noticia ,Contacto

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Periodista)
admin.site.register(Noticia)
admin.site.register(Contacto)
