from django.urls import path
from . import views
app_name = 'account'
urlpatterns = [
    path('signup', views.signup_form, name='signup_form'),
    path('login', views.login_form, name='login_form'),

]
