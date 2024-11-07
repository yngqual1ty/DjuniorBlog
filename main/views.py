from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Publication
from .forms import CreateBlogForm

def homepage(request):
    publications = Publication.objects.all().order_by('-date')
    if Publication.objects.all().order_by('-clickCount').count() < 3:
        popularPublications = Publication.objects.all().order_by('-clickCount')
    else:
        popularPublications = Publication.objects.all().order_by('-clickCount')[:3]
    return render(request, 'main/homepage.html', {'publications':publications, 'firstThreePublications':popularPublications})


def about(request):
    return render(request, 'main/about.html')


def blog(request, publicationId):
    publicationData = Publication.objects.get(id=publicationId)
    publicationData.clickCount += 1
    publicationData.save()

    return render(request, 'main/blog.html', {'publicationData':publicationData})

@login_required
def createBlog(request):
    error = ''
    if request.method == 'POST':
        form = CreateBlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            error = 'Неверно заполнена форма'

    form = CreateBlogForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/createBlog.html', context)

@login_required
def deleteBlog(request, publicationId):
    Publication.objects.get(id=publicationId).delete()
    return redirect('homepage')

@login_required
def editBlog(request, publicationId):
    error = ''
    if request.method == 'POST':
        form = CreateBlogForm(request.POST, instance=Publication.objects.get(id=publicationId))
        if form.is_valid():
            form.save()
            return redirect('homepage')

    form = CreateBlogForm(instance=Publication.objects.get(id=publicationId))
    context = {'form': form, 'error': error}
    return render(request, 'main/editBlog.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')