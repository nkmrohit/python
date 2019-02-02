from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from customerauth.forms import CustomersForm
from customerauth.models import Customers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login, authenticate
from django.contrib import auth

# Create your views here.
def create(request):
        
        
    if request.method=='POST':
        form = CustomersForm(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect('/customers/auth/list/')
        else:    
            return render(request,'customerauth/create.html',{'form':form})     
    else:
        form = CustomersForm()
        return render(request,'customerauth/create.html',{'form':form})

def edit(request,cst_id):
        instance = get_object_or_404(Customers,pk=cst_id);
        form = CustomersForm(request.POST or None, instance=instance)
        if request.method == 'POST':
                form = CustomersForm(request.POST or None, instance=instance)
                if form.is_valid():
                        form.save()
                        return  HttpResponseRedirect('/customers/auth/list')
                else:
                        form = CustomersForm(request.POST or None, instance=instance)
                        return render(request,'customerauth/update.html',{'form':form,'id':cst_id})    
        return render(request,'customerauth/update.html',{'form':form,'id':cst_id})    


def list(request):
        arguments = request.GET.get('q')
        if arguments:
                alldata =  Customers.objects.filter(fname__contains=arguments).all()
        else:
              alldata=  Customers.objects.all()     

        paginator = Paginator(alldata, 2) # Show 25 contacts per page
        page = request.GET.get('page')
        pagination = paginator.get_page(page)

        return render(request, 'customerauth/list.html',{'alldata':alldata,'pagination':pagination})

def detail(request,cst_id):
        cstdetail = get_object_or_404(Customers,pk=cst_id)
        return render(request, 'customerauth/detail.html',{'cstdetail':cstdetail})  

def delete(request, cst_id):
    Customers.objects.filter(id=cst_id).delete()
    return  HttpResponseRedirect('/customers/auth/list')

def login(request):
        username = password = ''
        if request.method=='POST':
                username = request.POST['username']
                password = request.POST['password']

                try:
                        customerId = Customers.objects.get(username=username)
                        customerUser = auth.authenticate(username=username, password=password)
                        if customerUser is not None:
                                request.session['member_id'] = customerId.id
                                request.session['logedin_user_type'] = 'customer'
                                auth.login(request, customerUser)
                                return  HttpResponseRedirect('/customers/auth/list')
                        else:
                                return render(request,'customerauth/login.html',{'args':'neeraj'})                
                except Exception as e:
                        return render(request,'customerauth/login.html',{'error':e})
        else:
                return render(request,'customerauth/login.html',{'args':'neeraj'})                
        