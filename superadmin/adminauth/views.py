from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def list(request):
    return HttpResponse('Hello Neeraj Maurya')