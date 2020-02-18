from django.shortcuts import render
from .models import Forbidden
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.


def table(request):
	return render(request, 'admin/tables.html')

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
