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


## 📁 Navegación de Documentos del Proyecto
El proyecto se encuentra divido en 2 fases
- 📄 Fase 01. Se presentara la documentacion inicial del diseno
- 📄 Fase 02. Se complementara la odcumentacion y se mostrara un prototipo funcional
- 📄 [Wiki](https://github.com/UESSalexmendoza/Diseno-Software/wiki)
### 🧭 Etapa 01 – Planificación y Coordinación
- 📄 [Acta de conformación del equipo](https://github.com/UESSalexmendoza/Diseno-Software/blob/main/Fase%201/Actas/01-Acta-de-Conformacion-del-Equipo.pdf)
- 📄 [Acta de reunión RF y RNF](https://github.com/UESSalexmendoza/Diseno-Software/blob/main/Fase%201/Actas/01-Acta-de-Reuni%C3%B3n-RF%20Y%20RNF.pdf)
- 📄 [Cronograma del Proyecto](https://github.com/UESSalexmendoza/Diseno-Software/blob/main/Fase%201/Documentacion/02-Cronograma.pdf)
- 📄 [Bitácora de decisiones (en Wiki)](https://github.com/UESSalexmendoza/Diseno-Software/wiki/Bit%C3%A1cora-de-Decisiones)
### 🔍 Etapa 02 – Análisis del Problema y Requerimientos
- 📄 [Visión del sistema](https://github.com/UESSalexmendoza/Diseno-Software/blob/main/Fase%201/Documentacion/04-Visi%C3%B3n%20del%20sistema.pdf)
- 📄 [Identificación de actores y funcionalidades](https://github.com/UESSalexmendoza/Diseno-Software/blob/main/Fase%201/Documentacion/03-%20Actores%20y%20funcionalidades.pdf)
- 📄 [Requerimientos funcionales y no funcionales](https://github.com/UESSalexmendoza/Diseno-Software/blob/main/Fase%201/Documentacion/05-Requerimientos%20funcionales%20y%20no%20funcionales.pdf)
### 🏗️ Etapa 03 – Diseño Arquitectónico
- 📄 [Documento de arquitectura de software](https://github.com/UESSalexmendoza/Diseno-Software/blob/main/Fase%201/Documentacion/04%20Diseno%20Arquitectonico.pdf)
- 📄 [Arquitectura de Seguridad](https://github.com/UESSalexmendoza/Diseno-Software/blob/main/Fase%201/Documentacion/05%20Diseno%20Arquitectonico%20-%20Seguridad.pdf)
---

## 🧾 Rúbricas de Evaluación

- 📄 [Rúbrica de evaluación – Alex Mendoza](https://github.com/UESSalexmendoza/Diseno-Software/blob/main/Fase%201/Rubricas/06-Rubrica-Evaluacion-Alex%20Mendoza.pdf)
- 📄 [Rúbrica de evaluación – Alejandro Cuenca](https://github.com/UESSalexmendoza/Diseno-Software/blob/main/Fase%201/Rubricas/06-Rubrica-Evaluacion-Alejandro%20Cuenca.pdf)
- 📄 [Rúbrica de evaluación – Oscar Vallejo](https://github.com/UESSalexmendoza/Diseno-Software/blob/main/Fase%201/Rubricas/06-Rubrica-Evaluacion-Oscar%20Vallejo.pdf)

---
## 🚀 Control y seguimiento

- 📄 [Evidencias para deciiones](https://github.com/UESSalexmendoza/Diseno-Software/discussions)
- 📄 [Bitacora de Pendientes](https://github.com/UESSalexmendoza/Diseno-Software/issues?q=is%3Aissue%20state%3Aclosed)

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
  
