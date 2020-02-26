from django.shortcuts import render
from django.contrib.auth import login ,get_user_model , logout

from django.http import HttpResponseRedirect

# Create your views here.
from .forms import UserCreationForm,UserLoginForm

User = get_user_model()	

def register(request, *args , **kwargs):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
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
		user = User.objects.get(username=request.POST['query'])
		request.session['user_id'] = user.id
		return HttpResponseRedirect("/")	

	context = {
		'form' : form
	}	
	return render(request,"Accounts/login.html",context)

def logout_view(request):
	try:
		del request.session['user_id']
	except KeyError:
		pass
	logout(request)
	message.info(request,"logged out successfully !")
	return HttpResponseRedirect("/login")