from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout

def signup_form (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # login(request, user)

            return redirect('Home:Home')
    else:
        form = UserCreationForm()
    return render (request, 'account/signup.html', {'form':form})

def login_form(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #login user
            user = form.get_user()
            login(request,user)
            return redirect('Home:Home')

    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html' ,{'form':form})


def logout_form (request):
    logout(request)
    return redirect('account:login_form')
