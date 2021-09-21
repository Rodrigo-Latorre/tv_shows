from django.shortcuts import render, HttpResponse, redirect
from datetime import date, datetime
from .models import Networks, Shows

def index(request):
  return redirect ('/register/')

def shows(request):
  context = {
    'shows': Shows.objects.all()
  }
  return render(request, 'index.html', context)

def new(request):
  context = {
    'networks': Networks.objects.all()
  }
  return render(request, 'new.html', context)

def create(request):
  show_title = request.POST['title']
  if request.POST['network'] == '-2':
    network = Networks.objects.create(name=request.POST['newnetwork'])
  else:
    network_id = request.POST['network']
    network = Networks.objects.get(id=network_id)
  show_release = request.POST['release']
  show_description = request.POST['description']
  Shows.objects.create(title=show_title,network=network,descr=show_description,release_date=show_release)
  return redirect('/shows/')

def shows_id(request, id):
  context = {
  'show': Shows.objects.get(id=id)
  }
  return render(request, 'detalle.html', context)

def edit(request, id):
  show = Shows.objects.get(id=id)
  fecha = show.release_date.strftime('%Y-%m-%d')
  context = {
  'show': show,
  'fecha': fecha,
  'networks': Networks.objects.all()
  }
  return render(request, 'edit.html', context)

def update(request, id):
  show = Shows.objects.get(id=id)
  show_title = request.POST['title']
  if request.POST['network'] == '-2':
    network = Networks.objects.create(name=request.POST['newnetwork'])
  else:
    network_id = request.POST['network']
    network = Networks.objects.get(id=network_id)
  show_release = request.POST['release']
  show_description = request.POST['description']
  show.title = show_title
  show.network = network
  show.release_date = show_release
  show.descr = show_description
  show.save()
  return redirect('/shows/')

def destroy(request, id):
  show = Shows.objects.get(id=id)
  show.delete()
  return redirect('/shows/')

def register(request):
  context = {
  'saludo': 'Hola'
  }
  return render(request, 'register.html', context)