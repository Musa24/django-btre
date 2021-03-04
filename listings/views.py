from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Listing


def index(request):
   listings = Listing.objects.all()
   for listing in listings:
       print(listing.list_date)
   context = {
       "listings":listings
   }
   return render(request,"listings/listings.html",context)

def listing(request,listing_id):
    template = loader.get_template("listings/listing.html")
    return HttpResponse(template.render())

def search(request):
    return render(request,"listings/search.html")