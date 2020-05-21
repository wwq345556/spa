from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.
def hello(request):
    return HttpResponse("Hello,world")

def orm(request):
    return HttpResponse("orm")

def flora_list(request):
    print(models)
    ret = models.FloraInfo.flora.all()
    name = ret[0].flora_name
    return HttpResponse(name)
    #return render(request, "publisher_list.html", {"publisher_list": ret})


def page_not_found(request,exception,template_name='testapp/404.html'):
	return render(request,template_name)

