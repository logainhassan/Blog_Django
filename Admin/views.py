from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from Admin.forms import UserForm,PostForm
from .models import *
from Admin.forms import UserForm , Category_form ,ForbiddenForm
from django.views.generic import  ListView

# Create your views here.


def table(request):
	all_users = User.objects.all()
	context ={'all_users' : all_users}
	return render(request, 'Admin/tables.html',context)


def addUser(request):
	if request.method == "POST":
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			user_form.save()
		return HttpResponseRedirect("/Admin/table")
	else:
		user_form =UserForm() 
		context = {'user_form':user_form}
		return render(request,'Admin/user.html',context)


def editUser(request,num):
	user = User.objects.get(id =num)
	if request.method == "POST":
		user_form = UserForm(request.POST,instance = user)
		if user_form.is_valid():
			user_form.save()
		return HttpResponseRedirect("/Admin/table")
	else:
		user_form = UserForm(instance = user)
		context = {'user_form':user_form}
		return render(request,'Admin/user.html',context)


def deleteUser(request,num):
	user = User.objects.get(id = num)
	user.delete()
	return HttpResponseRedirect("/Admin/table")



def user(request):
	# return render(request, 'Admin/user.html')
	form = UserForm()
	return render(request, 'Admin/user.html',{'form':form})


def Forbidden_Words(request):
	all_forbidden_words = Forbidden.objects.all()
	context = {'forbidden_words': all_forbidden_words}
	return render(request, 'Admin/forbidden_words.html', context)


def delete_forbidden_word(request, num):
	forbidden_word = Forbidden.objects.get(id = num)
	forbidden_word.delete()
	return HttpResponseRedirect('/Admin/Forbidden_Words')


def add_forbidden_word(request):
	form = ForbiddenForm()
	context = {'form': form}
	if request.method == "POST":
		form = ForbiddenForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/Admin/Forbidden_Words')
	return render(request, 'Admin/add_forbidden_word.html', context)

def edit_forbidden_word(request, num):
	f_word = Forbidden.objects.get(id = num)
	if request.method == "POST":
		form = ForbiddenForm(request.POST, instance = f_word)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/Admin/Forbidden_Words')
	form = ForbiddenForm(instance = f_word)
	context = {'form': form}
	return render(request, 'Admin/add_forbidden_word.html', context)

def all_Category(request):
	objects=Category.objects.all()
	fields=Category.get_model_fields(Category)
	context={
		'object_list' : objects ,
		 'fields' : fields ,
		 'title' : "Categories"
		 }
	return render(request,'Admin/Cat_table.html',context)



def edit_Category(request,num):
	cat_obj=Category.objects.filter(pk=num).first()
	if(request.method=="POST"):
		cat_form=Category_form(request.POST,instance=cat_obj)
		if cat_form.is_valid():
			cat_form.save()
		return HttpResponseRedirect	("/Admin/category")
	else:
		cat_form=Category_form(instance=cat_obj)
		context={
			'cat_form':cat_form,
			'title':'Edit'
			}
		
		return render(request,'Admin/category.html',context)

def delete_Category(request,num):
	cat_obj=Category.objects.filter(pk=num).first()
	cat_obj.delete()
	return HttpResponseRedirect("/Admin/category")


def add_Category(request):
	if request.method=="POST":
		cat_form=Category_form(request.POST)
		if cat_form.is_valid():
			cat_form.save()
		return HttpResponseRedirect("/Admin/category")	
	else:
		cat_form=Category_form()
		context={
			'cat_form':cat_form,
			'title':'Add'
			}
		return render(request,"Admin/category.html",context)

class Cat_searchResults(ListView):
	model=Category
	# queryset=Category.objects.filter(Name__icontains='Sports')
	template_name='Admin/Cat_table.html'
	def get_queryset(self):
		query=self.request.GET.get('q')
		object_list=Category.objects.filter(
		Name__icontains=query
		)
		return object_list
	def get_context_data(self,**kwargs):
		data = super().get_context_data(**kwargs)
		data['page_title'] = 'Authors'
		data['fields']=Category.get_model_fields(Category)
		return data

			
def posts(request):
	all_posts = Post.objects.all()

	context = {'all_posts':all_posts}
	return render(request,'Admin/posts.html',context)

def addPost(request):
	form = PostForm()
	if request.method=="POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/Admin/posts/')
	else:	
		context = {'form':form}
		return render(request,'Admin/add_post.html',context)

def editPost(request,num):
	post = Post.objects.get(id=num)
	if request.method=="POST":
		form = PostForm(request.POST, request.FILES,instance=post)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/Admin/posts/')
	else:
		form = PostForm(instance=post)
		context ={'form':form}
		return render(request,'Admin/edit_post.html',context)

def deletePost(request,num):
	post= Post.objects.get(id=num)
	post.delete()
	return HttpResponseRedirect('/Admin/posts/')

def post(request,num):
	post = Post.objects.get(post_id=num)
	context = {'post':post}
	return render(request,'admin/post.html',context)

# def postDetails(request,num):
# 	post = Post.objects.get(post_id=num)
# 	context = {'post':post}
# 	return render(request,'Admin/postDetails.html',context)

def allposts(request):
	post = Post.objects.all()
	context = {'post':post}
	return render(request,'Blog/posts.html',context)
