from django.shortcuts import render,HttpResponse,reverse
from . import models
# Create your views here.
# namayesh kool agahi
def Home (request,):
    show_ads = models.Divar.objects.all().order_by('-Date')
    return render(request, 'Home/home.html', {'show_ad':show_ads})
# namayesh link entekhabi
def detailshow (request,slug):
    return HttpResponse (slug)
