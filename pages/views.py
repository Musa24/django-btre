from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    print(request.path == "/")
    return render(request,"pages/index.html")


def about(request):
    # print("-------------------")
    # print('about1' in request.path)
    # print("-------------------")
    template = loader.get_template("pages/about.html") #Loading template
    return HttpResponse(template.render())       # rendering the template in HttpResponse  
