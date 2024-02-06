from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path('',views.index , name='index'),
    path('quickpredict',views.quickpredict , name='quickpredict'),
    path('signup',views.signup , name='signup'),
    path('signin',views.signin , name='signin'),
    path('signout',views.signout , name='signout'),
    path('contact',views.contact , name='contact'),
    path('about',views.about , name='about'),
    path('record', views.record , name='record'),
    path('prevention', views.prevention , name='prevention'),
    path('doctorhospital', views.doctorhospital , name='doctorhospital'),
    path('heartdetail',views.heartdetail,name='heartdetail'),
    path('symptoms', views.symptoms, name='symptoms'),
]
