from django.shortcuts import render
from .models import *

# Create your views here.


def table(request):
	return render(request, 'admin/tables.html')

def user(request):
	return render(request, 'admin/user.html')

def all_Category(request):
	objects=Category.objects.all()
	fields=Category.get_model_fields(Category)
	context={
		'Categories' : objects ,
		 'fields' : fields ,
		 'title' : "Categories"
		 }
	return render(request,'admin/tables.html',context)
