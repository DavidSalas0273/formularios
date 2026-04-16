from django.shortcuts import render, redirect
from .forms import SolicitudForm


def solicitud_create(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('solicitudes:confirmacion')
    else:
        form = SolicitudForm()
    return render(request, 'solicitudes/solicitud_form.html', {'form': form})


def solicitud_confirmacion(request):
    return render(request, 'solicitudes/solicitud_confirm.html')
