from multiprocessing import context
from .models import *
from django.http import HttpResponseRedirect
from django.shortcuts import render ,redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from .forms import *
from .filters import *
# Create your views here.


def index(request):
    stores = Store.objects.all()
    stores_count = stores.count()
    visit_form = 'visitform'
    store_filter = StoreFilter()
    
    context = {
        'test':'hello',
        'stores':stores,
        'stores_count':stores_count,
        'stores_filter':store_filter,
        'visit_form':visit_form,
        }
    return render(request,'home.html',context)

def store_list(request):
    stores = Store.objects.all()
    visit_list = Visit.objects.all()
    
    if request.GET:
        store_filter = StoreFilter(request.GET)
        stores = store_filter.qs
    else:
        store_filter = StoreFilter()
    
    all_stores = Store.objects.all()
    store_count = stores.count()
    context = {
        'stores':all_stores,
        'storess':stores,
        'count_stores':store_count,
        'stores_filter':store_filter,
        'visits':visit_list,
        
            }
    return render(request,'store_list.html',context)

def store_detail(request , slug):
    store = get_object_or_404(Store,slug=slug)
    form = VisitForm(instance=store)

    stores = Store.objects.all()
    if request.method == "POST":
        form = VisitForm(request.POST )
        if form.is_valid():
            #store = VisitForm(request.POST)
            #print(store)
            form.save()
            return redirect('/stores')
        else:
            form = VisitForm()
    else:
        form = VisitForm()

    context = {
        'store':store,
        'stores':stores,
        'form_visit':form,
    }

    return render(request,'store_detail.html',context)


def new_visit(request):
    form = VisitForm()

    stores = Store.objects.all()
    if request.method == "POST":
        form = VisitForm(request.POST)
        if form.is_valid():
            #store = VisitForm(request.POST)
            #print(store)
            form.save()
            return redirect('/stores')
        else:
            form = VisitForm()
    else:
        form = VisitForm()

    context = {
        'form_visit':form,
        'stores':stores,
    }
    return render(request,'visit/visit-new.html',context)

def visit_list(request):
    visits = Visit.objects.all()
    
    stores = Store.objects.all()
    visits_count = Visit.objects.count()
    store_count = Store.objects.count()
    context = {
        'stores':stores,
        'visits':visits,
        'visits_count':visits_count,
        'count_stores':store_count,

    }
    return render(request,'visit/list.html',context)

def visit_list_store(request,slug):
    
    stores = Store.objects.all()
    store = get_object_or_404(Store,slug=slug)
    visits_store = Visit.objects.filter(store=store)
    visits_store_count = Visit.objects.filter(store__slug=slug).count()
    context = {
        'store':store,
        'stores':stores,
        'visits':visits_store,
        'visits_count':visits_store_count,
    }

    return render(request,'visit/visit-list-store.html',context)



def profile(request):
    profile = Profile.objects.get(user=request.user)
    stores = Store.objects.all()
    print(request.path)
    print(profile)
    context = {
        'profile':profile,
        'stores':stores,
    }
    return render(request,'profile/profile.html',context)


def new_request(request,slug):
    store = get_object_or_404(Store,slug=slug)
    form = FixForm()
    context = { 'formfix' : form}
    return render(request,'request-new.html',context)
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