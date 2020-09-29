from django.urls import path
from . import views
app_name = 'account'
urlpatterns = [
    path('signup', views.signup_form, name = 'signup_form'),
    path('login' , views.login_form,  name = 'login_form' ),
    path('logout', views.logout_form, name = 'logout_form'),
    path('create', views.create_form, name = 'create_form'),


]
