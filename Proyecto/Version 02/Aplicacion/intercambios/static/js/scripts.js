/*!
* Start Bootstrap - Modern Business v5.0.7 (https://startbootstrap.com/template-overviews/modern-business)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-modern-business/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
document.addEventListener('DOMContentLoaded', function () {
  const botonesSolicitar = document.querySelectorAll('.solicitar-btn');

  botonesSolicitar.forEach(btn => {
    btn.addEventListener('click', function () {
      const libroId = this.dataset.libroId;
      if (!libroId) return;

      fetch(`/libros/${libroId}/solicitar-form/`)
        .then(response => response.text())
        .then(html => {
          const modalContainer = document.getElementById('modalSolicitudContent');
          modalContainer.innerHTML = html;

          const modalElement = document.getElementById('modalSolicitud');
          const modal = new bootstrap.Modal(modalElement);
          modal.show();

          // Evita que se quede el fondo oscuro si el modal se cierra manualmente
          modalElement.addEventListener('hidden.bs.modal', () => {
            document.querySelectorAll('.modal-backdrop').forEach(b => b.remove());
            document.body.classList.remove('modal-open');
            modalContainer.innerHTML = '';
          });

          // Fallback adicional si Bootstrap falla limpiando
          setTimeout(() => {
            document.body.classList.remove('modal-open');
            document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
          }, 500);
        });
    });
  });
});

document.addEventListener('DOMContentLoaded', function () {
    const modales = document.querySelectorAll('.modal');

    modales.forEach(modal => {
      modal.addEventListener('show.bs.modal', function (event) {
        const libroId = modal.getAttribute('data-libro-id');

        fetch(`/libros/${libroId}/incrementar-vista/`, {
          method: 'POST',
          headers: {
            'X-CSRFToken': '{{ csrf_token }}',
            'Content-Type': 'application/json'
          }
        })
        .then(response => response.json())
        .then(data => {
          console.log('Vista incrementada:', data);
        })
        .catch(error => {
          console.error('Error al incrementar vista:', error);
        });
      });
    });
  });

  document.addEventListener('DOMContentLoaded', function () {
  const botonesSolicitar = document.querySelectorAll('.solicitar-btn');
  
  botonesSolicitar.forEach(btn => {
    btn.addEventListener('click', function (e) {
      const requiereLogin = this.dataset.requiereLogin === "true";
      const libroId = this.dataset.libroId;

      if (requiereLogin) {
        window.location.href = "{% url 'login' %}?next={{ request.path }}";
      } else {
        fetch(`/libros/${libroId}/solicitar-form/`)
          .then(response => response.text())
          .then(html => {
            document.getElementById('modalSolicitudContent').innerHTML = html;
          })
          .catch(error => {
            console.error('Error al cargar el formulario:', error);
          });
      }
    });
  });
});


function actualizarEstado(peticionId, nuevoEstado) {
  const form = document.getElementById(`formEstado${peticionId}`);
  const respuesta = document.getElementById(`respuesta${peticionId}`).value;
  const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]').value;

  fetch(`/peticiones/${peticionId}/actualizar-estado/`, {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrfToken,
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      'estado': nuevoEstado,
      'respuesta': respuesta
    })
  })
  .then(res => res.json())
  .then(data => {
    if (data.success) {
      alert(`Petición actualizada a: ${nuevoEstado}`);
      location.reload();
    } else {
      alert('Error: ' + data.error);
    }
  })
  .catch(error => alert('Error del servidor'));
}
