from . import  views
from django.urls import path
urlpatterns =[
    # path('', views.reg,name="reg"),
    # path('about/',views.about,name="about"),   #here we use about/ instead of ' ' ...so when when we add about/ to the url, this will invokes
    # path('contact/',views.contact,name="contact"), #this is how we use more than one views
    # path('demo/',views.demo,name="demo")
    path('',views.index,name='index')
]
