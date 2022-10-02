from importlib.resources import path
from item_manager import views as item_manager_views
from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'home/index.html')
