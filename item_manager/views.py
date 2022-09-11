from importlib.resources import path
from django.shortcuts import render
from . import models

# Create your views here.
def item_new(request):
    if request.method == "POST":
        try:
            new_item = models.Item(
                name=request.POST.get('item_name'),
                description=request.POST.get('item_description'),
                item_cost_internal=request.POST.get('item_cost_internal')
            )
            new_item.save()
            message='Item created successfully'
        except:
            message='Error saving the item'
    else:
        message=''
    data = {
        'message': message
    }
    return render(request, 'item_manager/item_new.html', data)

def item_view(request):

    return render(request, 'item_manager/item_view.html')

def item_list(request):

    return render(request, 'item_manager/item_list.html')