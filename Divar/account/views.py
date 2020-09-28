from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def signup_form (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
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
            return redirect('Home:Home')

    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html' ,{'form':form})
