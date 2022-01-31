from .models import Store
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'test':'hello'}
    return render(request,'index.html',context)

def store_list(request):
    stores = Store.objects.all()
    store_count = Store.objects.count()
    context = {
        'stores':stores,
        'countstores':store_count,
            }
    return render(request,'store_list.html',context)