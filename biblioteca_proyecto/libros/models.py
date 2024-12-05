from django.db import models
from django import forms

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano_publicacion = models.IntegerField()
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'ano_publicacion', 'genero']
        labels = {
            'titulo': 'Título del Libro',
            'autor': 'Autor',
            'ano_publicacion': 'Año de Publicación',
            'genero': 'Género Literario',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el título del libro'
            }),
            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del autor'
            }),
            'ano_publicacion': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: 2024',
                'min': 1000,  # Para limitar a años válidos
                'max': 2024
            }),
            'genero': forms.Select(choices=[
                ('', 'Seleccione un género'),
                ('ficcion', 'Ficción'),
                ('no_ficcion', 'No Ficción'),
                ('poesia', 'Poesía'), 
                ('drama', 'Drama'),
                 ('literatura', 'Literatura'),
            ], attrs={
                'class': 'form-control'
            }),
        }

    def clean_ano_publicacion(self):
        ano = self.cleaned_data.get('ano_publicacion')
        if ano and (ano < 1000 or ano > 2024):
            raise forms.ValidationError("Por favor, ingrese un año válido entre 1000 y 2024.")
        return ano