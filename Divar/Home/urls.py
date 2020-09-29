from django.urls import path
from . import views
app_name ='Home'
urlpatterns = [
    path('', views.Home, name='Home'),
    path('/about_me', views.about_me, name='about_me'),
    path('/content', views.contact, name='content'), 
    path('<slug>', views.detailshow, name='detail_show'),


]
