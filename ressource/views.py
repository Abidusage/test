from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Ressource
from .forms import RessourceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages



def ressource(request):
    items = Ressource.objects.all()
    if request.method == 'POST':
        form = RessourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RessourceForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, "ressource/ressource.html", context)
@login_required(login_url='login')
def ajouter(request):
    items = Ressource.objects.all()
    if request.method == 'POST':
        form = RessourceForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('Ressource')
            messages.success(request, f'vous avez ajouter un ressource')
            return redirect('ajouter')
    else:
        form = RessourceForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'ressource/ajouter.html',context)
@login_required(login_url='login')
def delete_ressource(request,pk):
    items = Ressource.objects.get(id=pk)
    if request.method == 'POST':
        items.delete()
        return redirect('ajouter')
    return render(request, 'ressource/delete_ressource.html')

@login_required(login_url='login')
def update_ressource(request, pk):
    items = Ressource.objects.get(id=pk)
    if request.method == 'POST':
        form = RessourceForm(request.POST, instance= items)
        if form.is_valid():
            form.save()
            return redirect('ajouter')
    else:
        form = RessourceForm(instance= items)
    context={
        'form': form,

    }
    return render(request,'ressource/update_ressource.html', context)

@login_required(login_url='login')
def utilisateur(request):
    utilisateur = User.objects.all()
    context = {
        'utilisateur': utilisateur
    }
    return render(request, 'ressource/utilisateur.html', context)

@login_required(login_url='login')
def detail(request,pk):
    utilisateur = User.objects.get(id=pk)
    context ={
        'utilisateur': utilisateur
    }
    return render(request, 'ressource/detail.html', context)
