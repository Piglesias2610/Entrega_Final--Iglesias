from django.contrib import admin
from .models import Consola, Juego, Funko, Periferico

class ConsolaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "imagen")
    list_filter = ("nombre", "precio")
    ordering = ("nombre",)

class JuegoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "imagen")
    list_filter = ("nombre", "precio")
    ordering = ("nombre",)

class FunkoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "imagen")
    list_filter = ("nombre", "precio")
    ordering = ("nombre",)

class PerifericoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "imagen")
    list_filter = ("nombre", "precio")
    ordering = ("nombre",)

# Register your models here.
admin.site.register(Consola, ConsolaAdmin)
admin.site.register(Juego, JuegoAdmin)
admin.site.register(Funko, FunkoAdmin)
admin.site.register(Periferico, PerifericoAdmin)

