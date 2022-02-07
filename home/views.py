
from operator import index
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render

from home.models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        feedback=request.POST.get('feedback')
        contact=Contact(name=name,phone=phone,email=email,feedback=feedback)
        contact.save()
    return render(request,'contact.html')
