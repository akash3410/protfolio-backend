from django.shortcuts import render, redirect
from .models import ClientInfo
from .forms import RegisterForm, LoginForm, ClientInfoForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required

# Create your views here.
def superuser_or_staff_required(user):
    return user.is_superuser or user.is_staff

@user_passes_test(superuser_or_staff_required)
def profile_view(request):
    return render(request, 'clientapp/profile.html')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, "clientapp/registerForm.html", {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        form = LoginForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Access denied!")
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, "clientapp/loginForm.html", {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@user_passes_test(superuser_or_staff_required)
def client_info_view(request):
    user = request.user

    if not hasattr(user, 'clientinfo'):
        ClientInfo.objects.create(user=user)

    if request.method == "POST":
        form = ClientInfoForm(request.POST, request.FILES, instance=user.clientinfo)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ClientInfoForm(instance=user.clientinfo)

    context = {
        'form': form
    }

    return render(request, 'clientapp/clientinfoform.html', context)