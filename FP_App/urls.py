
from django.urls import path
from FP_App import views
from FP_App import forms

urlpatterns = [
    path('home/',views.first,name='Home'),
    path('about/',views.second,name='About'),
    # path('contact/',views.contact_form,name='Contact'),
    path('contact/',views.contact,name='Contact'),
    path('services/',views.sixth,name='Services'),
    path('gallery/',views.fourth,name='Gallery'),
    # path('users/',views.fivth,name='Users'),
    path('users/',views.users,name='Users'),



]
