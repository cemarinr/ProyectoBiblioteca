from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro, LibroForm

@login_required
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})
@login_required
def buscar_libros(request):
    query = request.GET.get('q')
    if query:
        resultados = Libro.objects.filter(titulo__icontains=query)  # Buscar por título (puedes ajustar para otros campos)
    else:
        resultados = Libro.objects.none()  # Si no hay búsqueda, no mostrar resultados
    return render(request, 'buscar_resultados.html', {'resultados': resultados, 'query': query})
@login_required
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'crear_libro.html', {'form': form})
@login_required
def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'editar_libro.html', {'form': form})
@login_required
def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'eliminar_libro.html', {'libro': libro})
