from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unathenticated_user 
from .forms import UserEditForm

@unathenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            messages.error(request, 'username or password are wrong')


    return render(request, 'user/login.html')

@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def editUser(request):
    form = UserEditForm(instance=request.user)

    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()


    context = {
        'form':form,
    }
    return render(request, 'user/user_form.html', context)