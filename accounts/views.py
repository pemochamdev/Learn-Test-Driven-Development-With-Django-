from django.shortcuts import render, redirect


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
    return render(request, 'accounts/login.html')