from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import SignUpForm
from .models import Room,Message

# Create your views here.

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.error(request, 'There was something wrong with logging in. Please try again...')
            return redirect('home')
    else:
        if request.user.is_authenticated:
            rooms = Room.objects.all()
            return render(request, 'home.html', {"rooms": rooms})
        else:
            return render(request, 'home.html')
    

def logout_u(request):
    logout(request)
    messages.success(request,'You have been Logged out Succesfully...')
    return redirect('home')    

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'You have Successfully Registered!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})


def room(request,slug):
    room_name=Room.objects.get(slug=slug).name
    messages=Message.objects.filter(room=Room.objects.get(slug=slug))
    
    return render(request, "room.html",{"room_name":room_name,"slug":slug,'messages':messages})