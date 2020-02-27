from django.shortcuts import render
from django.contrib.auth import login ,get_user_model , logout

from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from .forms import UserCreationForm,UserLoginForm, PasswordChangeForm


User = get_user_model()	

def register(request, *args , **kwargs):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "Configuration successfully submitted")
		return HttpResponseRedirect('../login')
	context = {
		'form' : form
	}

	return render(request,"Accounts/register.html",context)

def login_view(request, *args , **kwargs):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		user_obj = form.cleaned_data.get('user_obj')
		login(request,user_obj)
		return HttpResponseRedirect("/")	

	context = {
		'form' : form
	}	
	return render(request,"Accounts/login.html",context)

def logout_view(request):
	logout(request)
	#message.info(request,"logged out successfully !")
	return HttpResponseRedirect("../login")