from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
from django.http import HttpResponseRedirect
from .models import Forbidden
# Create your views here.


def home(request):
    return render(request , 'Blog_App/index.html')

