from django.shortcuts import render
from . import models
# Create your views here.
def Home (request,):
    show_ads = models.Divar.objects.all().order_by('-Date')
    return render(request, 'Home/home.html', {'show_ad':show_ads})
