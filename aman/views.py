from .models import *
from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
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

def store_detail(request , slug):
    store = get_object_or_404(Store,slug=slug)
    context = {
        'store':store
    }
    return render(request,'store_detail.html',context)

def new_request(request):
    pass
# def productlist(request , category_slug=None):
#     category = None
#     productlist = Product.objects.all()
#     categorylist = Category.objects.annotate(total_products=Count('product'))

#     if category_slug :
#         category = get_object_or_404(Category ,slug=category_slug)
#         productlist = productlist.filter(category=category)

#     search_query = request.GET.get('q')
#     if search_query :
#         productlist = productlist.filter(
#             Q(name__icontains = search_query) |
#             Q(description__icontains = search_query)|
#             Q(condition__icontains = search_query)|
#             Q(brand__brand_name__icontains = search_query) |
#             Q(category__category_name__icontains = search_query) 
#         )

#     paginator = Paginator(productlist, 1) # Show 25 contacts per page
#     page = request.GET.get('page')
#     productlist = paginator.get_page(page)
#     template = 'Product/product_list.html'

#     context = {'product_list' : productlist , 'category_list' : categorylist ,'category' : category }
#     return render(request , template , context)
