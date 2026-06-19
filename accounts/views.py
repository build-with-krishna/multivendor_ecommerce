from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def register_view(request):

    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            login(request, user)

            if user.role == 'vendor':
                return redirect('create_store')

            return redirect('home')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):

    error = ""

    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request,
                            username=email,
                            password=password)

        if user:
            login(request, user) 
            if user.role == 'vendor': 
                return redirect('vendor_dashboard') 
            return redirect('profile')

        else:
            error = "Invalid Email or Password"

    return render(request, 'accounts/login.html', {'error': error})


@login_required
def profile_view(request):

    return render(request, 'accounts/profile.html')


def logout_view(request):

    logout(request)
    return redirect('login')