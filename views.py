from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden

# Create your views here.


def home(request):
    return render(request, "aero_mx/home.html")
