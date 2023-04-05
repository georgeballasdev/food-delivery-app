from django.shortcuts import render, get_object_or_404
from .models import Store


def home(request):
    stores = Store.objects.all()
    context = {'stores': stores}
    return render(request, 'stores/home.html', context)

def store_detail(request, store_name):
    store_name = store_name.replace('-', ' ').title()
    store = get_object_or_404(Store, name=store_name)
    context = {
        'store': store
    }
    return render(request, 'stores/store.html', context)
