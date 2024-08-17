from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Ingresa un email válido")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("El email ya está en uso. Por favor, ingresa otro.")
        return email

class UserEditForm(UserChangeForm):
    password= None
    email=forms.EmailField(label="Ingrese su Email")
    first_name=forms.CharField(label="Apellido",required=False)
    last_name=forms.CharField(label="Nombre",required=False)
    imagen=forms.ImageField(required=False)

    class Meta:
        model=User
        fields=['email','last_name','first_name','imagen']