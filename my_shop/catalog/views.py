from django.shortcuts import render, redirect, get_object_or_404
from .models import Items
from .forms import ItemForm

def index(request):
    return render(request, 'catalog/index.html')

def item_list(request):
    items = Items.objects.all()
    return render(request, 'catalog/item_list.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'catalog/item_form.html', {'form': form, 'action': 'Add'})

def update_item(request, pk):
    item = get_object_or_404(Items, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'catalog/item_form.html', {'form': form, 'action': 'Update'})

def delete_item(request, pk):
    item = get_object_or_404(Items, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'catalog/item_confirm_delete.html', {'item': item})
