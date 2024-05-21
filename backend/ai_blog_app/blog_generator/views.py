from django.shortcuts import render
from django import views

# Create your views here.
def index(request):
    return render(request, 'index.html')
 
    
