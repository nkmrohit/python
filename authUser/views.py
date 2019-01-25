from django.shortcuts import render
from authUser import views
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.

def home(request):
    return render(request,'authUser/home.html',{'args':''})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            print(user)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'authUser/signup.html', {'form': form})

def login(request):

    if request.method=='POST':
        try:
            uid = User.objects.get(username=request.POST['username'])
            user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])

            if user is not None:
                request.session['member_id'] = uid.id
                auth.login(request, user)
                #return render(request, 'authUser/home.html', {'error':'Login success fully'})
                return redirect('home')
            else:
                return render(request, 'authUser/login.html', {'error':'Please enter correct user name and password'})
        except User.DoesNotExist:
            return render(request, 'authUser/login.html', {'error':'Please enter correct user name and password'})
 
    return render(request, 'authUser/login.html', {'error':''})

def logout(request):
    try:
        auth.logout(request)
        return render(request, 'authUser/login.html', {'error':'Logout Succesfully'})
    except KeyError:
        pass
    return HttpResponse("You're logged out.")


