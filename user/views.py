from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib import messages
from django.contrib.auth.models import User
from .import views
from django.contrib.auth import views as auth_view
# Create your views here.
def freelencing(request):
    workers = User.objects.all()
    context ={
        'workers': workers
    }
    return render(request, 'user/freelencing.html', context)
    
def voir_plus(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers,
    }
    return render(request, 'user/voir_plus.html', context)
def register(request):
    if request.method == 'POST':
        form =  CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'le compte à été crée pour  {username}. vous pouvez vous connecté')
            return redirect('login')
    else:
        form =  CreateUserForm()
    context = {
        'form': form,
    }
    return render(request, 'user/register.html',context)

@login_required(login_url='login')
def Profile(request):
    messages.success(request, f'Online')
    return render(request, 'user/Profile.html')

@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('Profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context ={
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'user/profile_update.html', context)