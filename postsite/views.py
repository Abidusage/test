from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Postsite
from django.contrib.auth.decorators import login_required
from .forms import PostsiteForm, PostsiteUpdateForm, CommentForm
# Create your views here.

def postsite(request):
    posts = Postsite.objects.all()
    if request.method == 'POST':
        form = PostsiteForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('postsite')
    else:
        form = PostsiteForm()
    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'postsite/postsite.html',context)
@login_required(login_url='login')
def postsite_detail(request, pk):
    posts = Postsite.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.posts = posts
            bginstance.save()
            return redirect('postsite_detail', pk=posts.id)
    else:
        c_form = CommentForm()
    context = {
        'posts': posts,
        'c_form': c_form,
    }
    return render(request, 'postsite/postsite_detail.html',context)
@login_required(login_url='login')
def postsite_edit(request, pk):
    posts = Postsite.objects.get(id=pk)
    if request.method == 'POST':
        form = PostsiteUpdateForm(request.POST, instance=posts)
        if form.is_valid():
            form.save()
            return redirect('postsite_detail', pk=posts.id)
    else:
        form = PostsiteUpdateForm(instance=posts)
    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'postsite/postsite_edit.html', context)
@login_required(login_url='login')
def postsite_delete(request, pk):
    posts = Postsite.objects.get(id=pk)
    if request.method == 'POST':
        posts.delete()
        return redirect('freelencing')
    context ={
        'posts': posts,
    }
    return render(request, 'postsite/postsite_delete.html',context)