from django.shortcuts import render, HttpResponse, redirect
from .models import Networks, Shows

def index(request):
    return redirect ('/shows/')

def shows(request):
    return render(request, 'index.html')

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
    # import pdb; pdb.set_trace()
    Shows.objects.create(title=show_title,network=network,descr=show_description,release_date=show_release)
    #
    #     atestring = show.release_date.strftime("%Y-%m-%d")

    return redirect('/shows/new')

def shows_id(request, id):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)

def edit(request, id):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)

def update(request, id):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)

def destroy(request, id):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)

