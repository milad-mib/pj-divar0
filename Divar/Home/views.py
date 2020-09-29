from django.shortcuts import render,HttpResponse,reverse
from . import models
# Create your views here.
# namayesh kool agahi
def Home (request,):
    show_ads = models.Divar.objects.all().order_by('-Date')
    return render(request, 'Home/home.html', {'show_ad':show_ads})
# namayesh link entekhabi
def detailshow (request,slug):
    # return HttpResponse (slug)
    show_detail = models.Divar.objects.get(slug=slug)
    return render (request, 'Home/show_detail.html', {'show_detail':show_detail}  )


def about_me(request):
    return render(request,'Home/about_me.html' )

def contact(request):
    return render(request ,'Home/contact.html' )
