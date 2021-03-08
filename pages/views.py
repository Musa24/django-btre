from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices,bedroom_choices,state_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published = True)[:3]
    
    context = {
        "listings":listings,
        "state_choice":state_choices,
        "bedroom_choices":bedroom_choices,
        "price_choices":price_choices
    }
    return render(request,"pages/index.html",context)

def about(request):
    realtors = Realtor.objects.order_by("-hire_date")
    mvp_realtor = Realtor.objects.filter(is_mvp = True)
    if mvp_realtor:
         mvp_realtor =  mvp_realtor[0]

    context = {
        "realtors":realtors,
        "mvp_realtor":mvp_realtor

    }
    template = loader.get_template("pages/about.html") #Loading template
    return HttpResponse(template.render(context))       # rendering the template in HttpResponse  
