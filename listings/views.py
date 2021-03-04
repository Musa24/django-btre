from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.template import loader
from .models import Listing



def index(request):
#    listings = Listing.objects.all()
   listings = Listing.objects.order_by("-list_date").filter(is_published=True)
   paginator = Paginator(listings,3)  # show X list per page
   page_number = request.GET.get("page")
   page_Obj = paginator.get_page(page_number)
   for listing in listings:
       print(listing.list_date)
   context = {
       "listings":page_Obj
   }
   return render(request,"listings/listings.html",context)

def listing(request,listing_id):
    template = loader.get_template("listings/listing.html")
    return HttpResponse(template.render())

def search(request):
    return render(request,"listings/search.html")


