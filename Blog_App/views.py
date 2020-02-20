from django.shortcuts import render
from Blog_App.forms import UserForm,PostForm
from Blog_App.models import Users,Posts
# Create your views here.


def table(request):
	all_users = Users.objects.all()
	context ={'all_users' : all_users}
	return render(request, 'admin/tables.html',context)

def user(request):
	form = UserForm()
	return render(request, 'admin/user.html',{'form':form})

