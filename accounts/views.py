from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from accounts.forms import UserRegistrationForm
def signup(request):
    form = UserRegistrationForm()
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)


def login_view(request):
    form = AuthenticationForm()
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(                
                username=username,
                password=password                
            )
            if user is not None:
                login(request, user)
            
            return redirect('home')
    
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)


def logout_views(request):
    logout(request)
    return redirect('home')