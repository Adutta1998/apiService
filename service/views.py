from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def home(req):
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))));
    return render(req,"home.html")
