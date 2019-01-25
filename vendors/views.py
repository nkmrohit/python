from django.shortcuts import render
from .forms import VendorForm
from django.http import HttpResponseRedirect, HttpResponse
from vendors.models import vendors

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save();
    else:
        form = VendorForm()        
    return render(request,'vendors/create.html',{'form':form})

def update(request):
    return render(request,'vendors/update.html',{'args':'Null'})

def list(request):
    allobjects = vendors.objects.all();
    print(allobjects)
    return render(request,'vendors/list.html',{'vendors':allobjects})

def detail(request,vendor_id):
    
    if vendor_id:
        vendor = vendors.objects.get(id=vendor_id)
        print(vendor);
        return render(request, 'vendors/detail.html', {'detail':vendor})
   
def delete(request):
    return render(request,'vendors/list.html',{'args':'Null'})    