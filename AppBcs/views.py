from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.core.mail import send_mail
from django.contrib import messages
def inicio(request):
    return render(request,"AppBcs/inicio.html")

class ConsolaListView(LoginRequiredMixin, ListView):
    model = Consola
    context_object_name = "consolas"
    template_name = "AppBcs/listar_consolas.html"


class ConsolaCreateView(LoginRequiredMixin, CreateView):
    model = Consola
    template_name = "AppBcs/create_consola.html"
    success_url = reverse_lazy("ListarConsolas")
    fields = ["nombre", "precio", "imagen"]

class ConsolaUpdateView(LoginRequiredMixin, UpdateView):
    model = Consola
    template_name = "AppBcs/update_consola.html"
    success_url = reverse_lazy("ListarConsolas")
    fields = ["nombre", "precio", "imagen"]

class ConsolaDeleteView(LoginRequiredMixin, DeleteView):
    model = Consola
    template_name = "AppBcs/borrar_consola.html"
    success_url = reverse_lazy("ListarConsolas")

# Lista los Periféricos
class PerifericoListView(LoginRequiredMixin, ListView):
    model = Periferico
    context_object_name = "perifericos"
    template_name = "AppBcs/listar_perifericos.html"

# Crea un Periférico
class PerifericoCreateView(LoginRequiredMixin, CreateView):
    model = Periferico
    template_name = "AppBcs/create_periferico.html"
    success_url = reverse_lazy("ListarPerifericos")
    fields = ["nombre", "tipo", "marca", "precio", "imagen"]

# Actualiza un Periférico
class PerifericoUpdateView(LoginRequiredMixin, UpdateView):
    model = Periferico
    template_name = "AppBcs/update_periferico.html"
    success_url = reverse_lazy("ListarPerifericos")
    fields = ["nombre", "tipo", "marca", "precio", "imagen"]

# Elimina un Periférico
class PerifericoDeleteView(LoginRequiredMixin, DeleteView):

    model = Periferico
    template_name = "AppBcs/borrar_periferico.html"
    success_url = reverse_lazy("ListarPerifericos")
   # Lista los Juegos
class JuegoListView(LoginRequiredMixin, ListView):
    model = Juego
    context_object_name = "juegos"
    template_name = "AppBcs/listar_juegos.html"

# Crea un Juego
class JuegoCreateView(LoginRequiredMixin, CreateView):
    model = Juego
    template_name = "AppBcs/create_juego.html"
    success_url = reverse_lazy("ListarJuegos")
    fields = ["nombre", "genero", "consola", "precio", "imagen"]

# Actualiza un Juego
class JuegoUpdateView(LoginRequiredMixin, UpdateView):
    model = Juego
    template_name = "AppBcs/update_juego.html"
    success_url = reverse_lazy("ListarJuegos")
    fields = ["nombre", "genero", "consola", "precio", "imagen"]

# Elimina un Juego
class JuegoDeleteView(LoginRequiredMixin, DeleteView):
    model = Juego
    template_name = "AppBcs/borrar_juego.html"
    success_url = reverse_lazy("ListarJuegos") 

class FunkoListView(LoginRequiredMixin, ListView):
    model = Funko
    context_object_name = "funkos"
    template_name = "AppBcs/listar_funkos.html"

# Crea un Funko
class FunkoCreateView(LoginRequiredMixin, CreateView):
    model = Funko
    template_name = "AppBcs/create_funko.html"
    success_url = reverse_lazy("ListarFunkos")
    fields = ["nombre", "personaje", "serie", "precio", "imagen"]

# Actualiza un Funko
class FunkoUpdateView(LoginRequiredMixin, UpdateView):
    model = Funko
    template_name = "AppBcs/update_funko.html"
    success_url = reverse_lazy("ListarFunkos")
    fields = ["nombre", "personaje", "serie", "precio", "imagen"]

# Elimina un Funko
class FunkoDeleteView(LoginRequiredMixin, DeleteView):
    model = Funko
    template_name = "AppBcs/borrar_funko.html"
    success_url = reverse_lazy("ListarFunkos")   

def presentacion(request):
    return render(request, 'AppBcs/presentacion.html') 


