from importlib.resources import path
from django.shortcuts import render

# Create your views here.
def new(request):

    return render(request, 'customer_pricing_manager/customer_pricing_new.html')

def view(request):

    return render(request, 'customer_pricing_manager/customer_pricing_view.html')

def list(request):

    return render(request, 'customer_pricing_manager/customer_pricing_list.html')
