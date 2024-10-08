from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    home = Home.objects.all().order_by('-id')
     
    return render(request, 'index.html', {'home': home})
