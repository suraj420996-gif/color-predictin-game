from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Wallet
from decimal import Decimal
from django.contrib.auth.decorators import login_required



def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'account/signup.html', {
                "error": "Username already taken, please choose another!"
            })

        user = User.objects.create_user(username=username, password=password)
        Wallet.objects.create(user=user)
        login(request, user)
        return redirect('/game/play/')

    return render(request, 'account/signup.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
        return redirect('/game/play/')
    return render(request, 'account/login.html')
def logout_view(request):
    logout(request)
    return redirect('/account/login/')

