# 📚 Proyecto Biblioteca

Un sistema web desarrollado con Django que permite gestionar un club de biblioteca. Este proyecto incluye funcionalidades como la creación, edición y eliminación de libros, búsqueda avanzada, autenticación básica (login), y personalización de la interfaz con modo oscuro.

---

## 📜 Descripción breve

Este sistema está diseñado para facilitar la gestión de una biblioteca, proporcionando herramientas esenciales como:
- Listado, creación, edición y eliminación de libros.
- Funcionalidad de búsqueda de libros mediante un formulario.
- Autenticación básica con un usuario administrador predeterminado.
- Uso de una base HTML común para un diseño consistente en todas las páginas.
- Alternar entre modo oscuro y claro para mejorar la experiencia del usuario.

---

## 🖼️ Requisitos del sistema

- Python 3.8 o superior.
- Django 4.x o superior.
- Sistema operativo: Windows, macOS o Linux.
- Navegador moderno (Chrome, Firefox, Edge, etc.).

---

## 🛠️ Estructura del proyecto

```
biblioteca_proyecto/
├── biblioteca_proyecto/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── libros/
│   ├── __pycache__/
│   ├── migrations/
│   ├── static/
│   │   └── css/
│   │       └── estilos.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── buscar_resultados.html
│   │   ├── crear_libro.html
│   │   ├── editar_libro.html
│   │   ├── eliminar_libro.html
│   │   └── lista_libros.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
├── db.sqlite3
├── manage.py
├── readme.md
├── requirements.txt
├── capturas_pantalla/
│   ├── ACTUALIZAR_LIBRO.png
│   ├── ELIMINAR_LIBRO.png
│   ├── GUARDAR_LIBRO.png
│   ├── LOGIN.png
│   └── LISTA_LIBROS.png
└── venv/
    ├── Include/
    ├── Lib/
    ├── Scripts/
    └── pyvenv.cfg
```

---

## 🔧 Instrucciones de instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/cemarinr/ProyectoBiblioteca.git
   ```
2. Accede al directorio del proyecto:
   ```bash
   cd proyecto_biblioteca
   ```

---

## 🚧 Configuración del entorno virtual

1. Crea un entorno virtual:
   ```bash
   python -m venv venv
   ```
2. Activa el entorno virtual:
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

---

## 📦 Instalación de dependencias

Instala las dependencias requeridas desde el archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución del proyecto

1. Realiza las migraciones iniciales de la base de datos:
   ```bash
   python manage.py migrate
   ```
2. Crea un usuario administrador:
   ```bash
   python manage.py createsuperuser
   ```
   Credenciales sugeridas:
   - **Usuario**: `admin`
   - **Contraseña**: `admin`
3. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```
4. Abre el navegador y accede a:
   - **Página principal**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - **Panel de administración**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📘 Funcionalidades principales

### 1. **Lista de libros**
Visualiza una lista de libros disponibles en la biblioteca.

### 2. **Buscador de libros**
Realiza búsquedas rápidas de libros mediante un formulario en la barra de navegación.

### 3. **Modo oscuro**
Alterna entre los modos oscuro y claro para mejorar la experiencia visual del usuario.

### 4. **Login básico**
Autenticación básica con credenciales estándar (usuario: `admin`, contraseña: `admin`).

### 5. **Plantilla base reutilizable**
Se utiliza un diseño consistente para todas las páginas mediante una plantilla base (`base.html`).

---

## 🖼️ Capturas de pantalla

### Lista de libros
![Lista de libros](capturas_pantalla/LISTA_LIBROS.png)

### Guardar un libro
![Guardar libro](capturas_pantalla/GUARDAR_LIBRO.png)

### Editar un libro
![Actualizar libro](capturas_pantalla/ACTUALIZAR_LIBRO.png)

### Inicio de sesión
![Inicio de sesión](capturas_pantalla/LOGIN.png)

---

## 🛡️ Información de contacto

- **Nombre**: Carlos Estiven Marin Ruiz
- **Email**: cemarinr@itc.edu.co
- **LinkedIn**: [linkedin.com/in/carlos-marin](www.linkedin.com/in/estivenmarinn)

👋¡Gracias por visitar el proyecto!