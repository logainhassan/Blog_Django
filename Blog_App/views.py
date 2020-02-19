from django.shortcuts import render
from .models import *
from Blog_App.forms import UserForm
from Blog_App.models import Users,Posts
from django.http import HttpResponseRedirect

# Create your views here.


def table(request):
	all_users = Users.objects.all()
	context ={'all_users' : all_users}
	return render(request, 'admin/tables.html',context)


def addUser(request):
	if request.method == "POST":
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			user_form.save()
		return HttpResponseRedirect("/Blog_App/table")
	else:
		user_form =UserForm() 
		context = {'user_form':user_form}
		return render(request,'admin/user.html',context)


def editUser(request,num):
	user = Users.objects.get(user_id =num)
	if request.method == "POST":
		user_form = UserForm(request.POST,instance = user)
		if user_form.is_valid():
			user_form.save()
		return HttpResponseRedirect("/Blog_App/table")
	else:
		user_form = UserForm(instance = user)
		context = {'user_form':user_form}
		return render(request,'admin/user.html',context)


def deleteUser(request,num):
	user = Users.objects.get(user_id = num)
	user.delete()
	return HttpResponseRedirect("/Blog_App/table")



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
	return render(request,'admin/Cat_table.html',context)
