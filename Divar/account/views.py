from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from Home import models
from django.contrib.auth.decorators import login_required
from . import forms

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
            if 'next' in request.POST:
                #next pege
                return redirect(request.POST.get('next'))
            else:
                return redirect('Home:Home')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html' ,{'form':form})

def logout_form (request):
    logout(request)
    return redirect('account:login_form')

@login_required(login_url="account:login_form")
def create_form(request):
    if request.method == 'POST':
        form = forms.create_form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.Author = request.user
            instance.save()
            #save cread

            return redirect('Home:Home')
    else:
        form = forms.create_form()
    return render (request,'account/create.html', {'form':form})
