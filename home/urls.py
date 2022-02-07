from xml.etree.ElementInclude import include
from django import views
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('about',views.about,name='about'),
    path('',views.index,name='index'),
    
    path('contact',views.contact,name='contact')
]
admin.site.site_header = "BAKERY ADMIN"
admin.site.site_title = "Bakery Admin Portal"
admin.site.index_title = "Welcome to Bakery Portal"