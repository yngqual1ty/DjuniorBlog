from tarfile import data_filter

from django.shortcuts import render
from .models import Publication
def homepage(request):
    publications = Publication.objects.all().order_by('-date')
    if Publication.objects.all().order_by('-clickCount').count() < 3:
        popularPublications = Publication.objects.all().order_by('-clickCount')
    else:
        popularPublications = Publication.objects.all().order_by('-clickCount')[:3]
    return render(request, 'main/homepage.html', {'publications':publications, 'firstThreePublications':popularPublications})

def about(request):
    return render(request, 'main/about.html')