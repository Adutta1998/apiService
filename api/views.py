from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def apiAll(req):
    return HttpResponse("Api")
