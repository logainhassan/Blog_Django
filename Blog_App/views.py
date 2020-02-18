from django.shortcuts import render
from .models import Forbidden
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from Blog_App.forms import UserForm, ForbiddenForm
from Blog_App.models import Users,Posts
# Create your views here.


def table(request):
	all_users = Users.objects.all()
	context ={'all_users' : all_users}
	return render(request, 'admin/tables.html',context)

def user(request):
	return render(request, 'admin/user.html')


def Forbidden_Words(request):
	all_forbidden_words = Forbidden.objects.all()
	context = {'forbidden_words': all_forbidden_words}
	return render(request, 'admin/forbidden_words.html', context)


def delete_forbidden_word(request, num):
	forbidden_word = Forbidden.objects.get(id = num)
	forbidden_word.delete()
	return HttpResponseRedirect('/Blog_App/Forbidden_Words')


def add_forbidden_word(request):
	form = ForbiddenForm()
	context = {'form': form}
	if request.method == "POST":
		form = ForbiddenForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/Blog_App/Forbidden_Words')
	return render(request, 'admin/add_forbidden_word.html', context)