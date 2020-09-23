from django.shortcuts import render,HttpResponse

# Create your views here.
def login_view (request,):
    return HttpResponse('WelCome to login_view')
