from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.core import exceptions
from vendorauth.forms import VendorsForm
from vendorauth.models import vendors
from django.contrib.auth import login, authenticate
from django.contrib import auth
from django.conf import settings

# Create your views here.
def create(request):
        
        
    if request.method=='POST':
        form = VendorsForm(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/vendors/auth/list/')
        else:    
            print(form)
            return render(request,'vendorauth/create.html',{'form':form})     
    else:
        form = VendorsForm()
        return render(request,'vendorauth/create.html',{'form':form})

def edit(request,cst_id):
        instance = get_object_or_404(vendors,pk=cst_id);
        form = VendorsForm(request.POST or None, instance=instance)
        if request.method == 'POST':
                form = VendorsForm(request.POST or None, instance=instance)
                if form.is_valid():
                        form.save()
                        return  HttpResponseRedirect('/vendors/auth/list')
                else:
                        form = VendorsForm(request.POST or None, instance=instance)
                        return render(request,'vendorauth/update.html',{'form':form,'id':cst_id})    
        return render(request,'vendorauth/update.html',{'form':form,'id':cst_id})    


def list(request):
        arguments = request.GET.get('q')
        request.session['logedin_user_type']=' '
        if arguments:
                alldata =  vendors.objects.filter(fname__contains=arguments).all()
        else:
              alldata=  vendors.objects.all()     

        paginator = Paginator(alldata, 2) # Show 25 contacts per page
        page = request.GET.get('page')
        pagination = paginator.get_page(page)
        sessionValue = request.session['logedin_user_type']
        
        return render(request, 'vendorauth/list.html',{'alldata':alldata,'pagination':pagination})

def detail(request,cst_id):
        cstdetail = get_object_or_404(vendors,pk=cst_id)
        return render(request, 'vendorauth/detail.html',{'cstdetail':cstdetail})  

def delete(request, cst_id):
    vendors.objects.filter(id=cst_id).delete()
    return  HttpResponseRedirect('/vendors/auth/list')

############################# Vendor Login ####################################    
def login(request):
        username = password = ' '
        request.session['logedin_user_type']=' '
        if request.method=='POST':
                try:        
                        username = request.POST['username']
                        password = request.POST['password']
                        vendorId = vendors.objects.get(username=username)
                        #settings.configure(AUTH_USER_MODEL ='vendors.vendorauth.vendors')
                        #settings.configure(AUTH_USER_MODEL,'vendors.vendorauth.vendors')
                        VendorUser = auth.authenticate(username=username, password=password)
                        if VendorUser is not None:

                                request.session['member_id'] = vendorId.id
                                request.session['logedin_user_type'] = 'vendor'
                                auth.login(request, VendorUser)
                                return  HttpResponseRedirect('/vendors/auth/list')
                        else:
                                return render(request,'vendorauth/login.html',{'args':'neeraj'})                
                except Exception as e:
                        return render(request,'vendorauth/login.html',{'args':'neeraj'})                

        else:
                return render(request,'vendorauth/login.html',{'args':'neeraj'})                
        
