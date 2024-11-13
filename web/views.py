from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.contrib import messages # type: ignore

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request,"Logged In !!!")
            return redirect('home')
        else:
            messages.success(request, "Not Logged In !!!")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request,"Logged Out ....")
    return redirect('home')