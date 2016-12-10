from django.shortcuts import render
from Blog.models import Art
from django.views.generic import ListView

def listpost(request):
	lista = Art.objects.all()
	return render(request, 'templates/index.html', {'lista':lista})

def detalle(request, id):
	try:
		lista = Art.objects.get(id=id)
	except Art.DoesNotExist:
		lista = 'no existe'
	return render(request, 'templates/detalle.html', {'lista': lista})

class List(ListView):
	model = Art
	template_name = 'templates/index.html'