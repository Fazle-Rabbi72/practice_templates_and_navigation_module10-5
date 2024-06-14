from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d={'author':'fazle Rabbi','age':20,'lst':['a','b','c'],'born':datetime.datetime.now(),'course':'python is fun','list':['apple','mango','orange']}
    return render(request,'home.html',d)