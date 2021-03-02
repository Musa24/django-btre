from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
   return render(request,"listings/listings.html")

def listing(request):
    template = loader.get_template("listings/listing.html")
    return HttpResponse(template.render())

def search(request):
    return render(request,"listings/search.html")