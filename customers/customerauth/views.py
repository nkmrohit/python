from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from customerauth.forms import CustomersForm
from customerauth.models import Customers

# Create your views here.
def Create(request):
    if request.method=='POST':
        form = CustomersForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomersForm()
        return render(request,'customerauth/create.html',{'form':form})
  
def list(request):
        return render(request, 'customerauth/list.html',{'args':'neeraj'})