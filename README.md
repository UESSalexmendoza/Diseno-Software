# 📚 Plataforma de Trueque de Libros – Equipo 8

Proyecto desarrollado como parte de la asignatura **“Del Diseño al Prototipo: Construyendo Software Colaborativamente”**. El objetivo principal es aplicar principios y prácticas de diseño de software mediante un proceso estructurado y colaborativo, utilizando herramientas modernas de desarrollo y control de versiones.

---

## 🎯 Objetivo General

Diseñar y desarrollar un prototipo funcional de una plataforma web que permita a estudiantes **publicar, buscar e intercambiar libros** entre ellos, facilitando el acceso a material de estudio de manera colaborativa.

---

## ✨ Funcionalidades clave

- Registro de libros disponibles para trueque.
- Búsqueda por título, autor o categoría.
- Visualización de detalles de los libros.
- Contacto entre estudiantes para gestionar el intercambio.
- Edición y eliminación de publicaciones propias.

---

## 👥 Integrantes del equipo

- **Alex Mendoza Morante** – Líder de Proyecto  
- **Oscar Vallejo Miño** – Arquitecto del Sistema  
- **Bryan Cuenca Guerrero** – Analista del Sistema

---

## 🛠️ Tecnologías utilizadas

- **Lenguaje**: Python 3.10+
- **Framework**: Django
- **Base de datos**: MySQL
- **Control de versiones**: Git + GitHub

---

## 🚀 ¿Cómo ejecutar el prototipo?

### 🔧 Requisitos previos

- Python 3.10 o superior
- MySQL Server instalado y en ejecución
- Entorno virtual (opcional pero recomendado)

### 📦 Instalación

1. **Clona este repositorio**
   ```bash
   git clone https://github.com/UESSalexmendoza/Diseno-Software.git
   cd Diseno-Software
2. **Crea y activa un entorno virtual**
   ```bash
   python -m venv env
   source env/bin/activate      # En Windows: env\Scripts\activate
3. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
4. **Crea la base de datos en MySQL**
   ```bash
   CREATE DATABASE trueque_libros;
5. **Configura tus credenciales de base de datos**
- Abre Diseno-Software/settings.py y actualiza la sección DATABASES con tu usuario y contraseña.
6. Aplica las migraciones
   ```bash
   python manage.py makemigrations
   python manage.py migrate
7. Ejecuta el servidor
   ```bash
   python manage.py runserver
8. Abre en el navegador
   - http://localhost:8000
  
