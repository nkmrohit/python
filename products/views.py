from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import product
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def list(request):
    requestArg = request.GET.get('q')
    if requestArg:
       contact_list = product.objects.filter(Title__contains=requestArg).all()
    else:
        contact_list = product.objects.all()

    paginator = Paginator(contact_list, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    return render(request, 'products/list.html', {'args':contact_list,'contacts':contacts })

@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        if request.POST['name']:
            products = product()
            products.Title =  request.POST['name']
            products.body =  request.POST['body']
            products.url ='http://' + request.POST['url']
            products.icon =  request.FILES['icon']
            products.image =  request.FILES['image']
            products.pub_date = timezone.datetime.now()
            products.user = request.user
            products.summary = request.POST['summary']    
            products.votes_total = 1        
            products.save()
            return redirect('details/'+str(products.id))
        else:
            return render(request, 'products/create.html', {'error':'Please fill all mandatory fields'} )    
    return render(request, 'products/create.html', {'error':''} )    

def details(request, product_id):
    products = get_object_or_404(product,pk=product_id)
    #products =  product.objects.get(pk=product_id)
    return render(request, 'products/detail.html', {'product':products})

@login_required(login_url='login')
def edit(request, product_id):
    products = get_object_or_404(product,pk=product_id)
    #products =  product.objects.get(pk=product_id)
    if request.method == 'POST':
        products.Title =  request.POST['name']
        products.body =  request.POST['body']
        products.url ='http://' + request.POST['url']
        #if request.POST['icon']:
        #    products.icon =  request.FILES['icon']
        #if request.POST['image']:
        #    products.image =  request.FILES['image']
        products.pub_date = timezone.datetime.now()
        products.user = request.user
        products.summary = request.POST['summary']    
        products.votes_total = 1        
        products.save()
        return redirect('/product/details/'+str(products.id))
    return render(request, 'products/edit.html', {'product':products})    

def delete(request, product_id):
    product.objects.filter(id=product_id).delete()
    return redirect('/product/list')    
