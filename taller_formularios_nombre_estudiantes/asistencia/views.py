from django.shortcuts import render, redirect
from .forms import AsistenciaForm


def asistencia_create(request):
	if request.method == 'POST':
		form = AsistenciaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('asistencia:confirmacion')
	else:
		form = AsistenciaForm()
	return render(request, 'asistencia/asistencia_form.html', {'form': form})


def asistencia_confirmacion(request):
	return render(request, 'asistencia/asistencia_confirm.html')
