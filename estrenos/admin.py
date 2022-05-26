from django.contrib import admin
from estrenos.models import Usuario, Pelicula

# Register your models here.


class PeliculaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "link")
    search_fields = ("titulo", "usuarios__usuario")
    list_filter = ("usuarios__usuario",)


admin.site.register(Pelicula, PeliculaAdmin)
