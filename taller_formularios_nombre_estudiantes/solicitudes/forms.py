from django import forms
from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'nombre_solicitante',
            'documento_identidad',
            'correo_electronico',
            'telefono',
            'tipo_solicitud',
            'asunto',
            'descripcion',
            'fecha_solicitud',
            'archivo_adjunto',
        ]
        widgets = {
            'nombre_solicitante': forms.TextInput(attrs={
                'placeholder': 'Ej: Juan Pérez',
                'autocomplete': 'name',
            }),
            'documento_identidad': forms.TextInput(attrs={
                'placeholder': 'Ej: 1234567890',
            }),
            'correo_electronico': forms.EmailInput(attrs={
                'placeholder': 'correo@ejemplo.com',
                'autocomplete': 'email',
            }),
            'telefono': forms.TextInput(attrs={
                'placeholder': 'Ej: 300 123 4567',
                'autocomplete': 'tel',
            }),
            'tipo_solicitud': forms.Select(attrs={
                'class': 'select-field',
            }),
            'asunto': forms.TextInput(attrs={
                'placeholder': 'Resumen breve de su solicitud',
            }),
            'descripcion': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Describa detalladamente su solicitud...',
            }),
            'fecha_solicitud': forms.DateInput(attrs={
                'type': 'date',
            }),
            'archivo_adjunto': forms.ClearableFileInput(attrs={
                'accept': '.pdf,.doc,.docx,.jpg,.jpeg,.png',
            }),
        }
        labels = {
            'nombre_solicitante': 'Nombre completo',
            'documento_identidad': 'Documento de identidad',
            'correo_electronico': 'Correo electrónico',
            'telefono': 'Teléfono de contacto',
            'tipo_solicitud': 'Tipo de solicitud',
            'asunto': 'Asunto',
            'descripcion': 'Descripción detallada',
            'fecha_solicitud': 'Fecha de la solicitud',
            'archivo_adjunto': 'Archivo adjunto (opcional)',
        }
