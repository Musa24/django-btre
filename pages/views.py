from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published = True)[:3]
    
    context = {
        "listings":listings
    }
    return render(request,"pages/index.html",context)

def about(request):
    realtors = Realtor.objects.order_by("-hire_date")
    mvp_realtor = Realtor.objects.filter(is_mvp = True)[0]

    context = {
        "realtors":realtors,
        "mvp_realtor":mvp_realtor

    }
    template = loader.get_template("pages/about.html") #Loading template
    return HttpResponse(template.render(context))       # rendering the template in HttpResponse  
