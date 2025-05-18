from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordChangeForm

from .models import Usuario, Contacto, Libro

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Usuario',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña',
        })

class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
            'id': 'id_email'
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        UserModel = get_user_model()
        if not UserModel.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError(_("No existe ninguna cuenta activa con este correo electrónico."))
        return email
    

class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nueva contraseña',
            'id': 'new_password1',
        })

        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña',
            'id': 'new_password2',
        })    



class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'username', 'email', 'first_name', 'last_name',
            'password1', 'password2',
            'nombreReal', 'telefono', 'fecha_nacimiento',
            'aceptacionPolitica', 'contactoPrincipal',
        ]
        widgets = {
            'aceptacionPolitica': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f'{existing_classes} form-control'.strip()
                field.widget.attrs['placeholder'] = field.label

# forms.py
class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'first_name', 'last_name',
            'email', 'nombreReal', 'telefono',
            'fecha_nacimiento', 'contactoPrincipal'
        ]
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_classes} form-control'.strip()
            field.widget.attrs['placeholder'] = field.label


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombres', 'apellidos', 'correo', 'telefono', 'comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={
                'rows': 4,
                'maxlength': 1000,
                'style': 'resize: none;height: 120px;',
                'class': 'form-control',
                'placeholder': 'Escribe tu comentario u observación...',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'comentario':  # Ya configurado arriba
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['placeholder'] = field.label

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            existing_classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing_classes} form-control'.strip()
            field.widget.attrs['placeholder'] = field.label


        
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['nombre', 'descripcion', 'autor','editorial', 'categoria', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Describe brevemente tu libro',
                'class': 'form-control'
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.ClearableFileInput):
                field.widget.attrs.update({'class': 'form-control', 'accept': 'image/*'})
            else:
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f'{existing_classes} form-control'.strip()
                field.widget.attrs['placeholder'] = field.label

class SolicitudIntercambioForm(forms.Form):
    libro_ofrecido = forms.ModelChoiceField(
        queryset=Libro.objects.none(),
        label='Selecciona tu libro',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Selecciona un libro'
        })
    )
    mensaje = forms.CharField(
        required=False,
        label='Mensaje o comentario adicional',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Mensaje o comentario'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            existing = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{existing} form-control'.strip()
            field.widget.attrs['placeholder'] = field.label
