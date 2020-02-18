from django.shortcuts import render

# Create your views here.


def table(request):
	return render(request, 'admin/tables.html')

def user(request):
	return render(request, 'admin/user.html')
