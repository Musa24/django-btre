from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.template import loader
from .models import Listing
from .choices import price_choices,bedroom_choices,state_choices


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
    listing = get_object_or_404(Listing,pk  = listing_id)
    context = {
        "listing":listing
    }
    template = loader.get_template("listings/listing.html")
    return HttpResponse(template.render(context))

def search(request):
    queryset_list = Listing.objects.order_by("-list_date")
    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    
    #city
    if 'city' in request.GET:
        city = request.GET["city"]
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    # state
    if "state" in request.GET:
        state = request.GET["state"]
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
    
    #bedroom
    if "bedrooms" in request.GET:
        bedrooms = request.GET["bedrooms"]
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  #bedroom
    if "price" in request.GET:
        price = request.GET["price"]
        if price:
            queryset_list = queryset_list.filter(price__lte=price)


    context = {
        "state_choices":state_choices,
        "bedroom_choices":bedroom_choices,
        "price_choices":price_choices,
        "listings":queryset_list,
        "values":request.GET
    }
    return render(request,"listings/search.html",context)
