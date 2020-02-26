from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse ,HttpResponseRedirect
from Admin.forms import PostForm,UserCreationForm,UserChangeForm
from .models import *
from Admin.forms import *

from django.views.generic import  ListView

# Create your views here.


def user(request):
	all_users = MyUser.objects.all()
	context ={'all_users' : all_users}
	return render(request, 'Admin/tables.html',context)


def addUser(request):
	form = UserCreationForm()
	if request.method=="POST":
		form = UserCreationForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/Admin/users/')

	context = {'form':form}
	return render(request,'Admin/user.html',context)

def editUser(request,num):
	user = MyUser.objects.get(id =num)
	form = UserChangeForm(instance = user)
	print("formaaak       " ,user.avatar.url)
	if request.method == "POST":
		form = UserChangeForm(request.POST ,request.FILES ,instance = user)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/Admin/users")

	context = {'form':form,'avatar':user.avatar.url}
	return render(request,'Admin/edit_user.html',context)


def deleteUser(request,num):
	user = User.objects.get(id = num)
	user.delete()
	return HttpResponseRedirect("/Admin/users")


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
	post = Posts.objects.get(post_id=num)
	context = {'post':post}
	return render(request,'Admin/post.html',context)


# def tags(request):
#     tags=Tag.objects.all()
# 	context={
# 		'tags': tags
# 		}
# 	return render(request,'Admin/tags.html',context)

def tags(request):
	tags=Tag.objects.all()
	fields=Tag.get_model_fields(Tag)
	context={
		'object_list':tags,
		'fields':fields,
		'title':'Tags'
		}
	return render(request,'Admin/tags.html',context)

def add_tag(request):
	form=TagForm()
	if request.method=='POST':
		form=TagForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect("/Admin/tags/")
	else:
		context={
			'TagForm':form,
			'title':'Add'
			}
		return render(request,'Admin/tag.html',context)


	

def edit_tag(request,num):
	form=TagForm()
	tag=Tag.objects.get(pk=num)
	if request.method=='POST':
		form=TagForm(request.POST,instance=tag)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/Admin/tags/')
	else:
		form=TagForm(instance=tag)
		context={
			'TagForm':form,
			'title':'Edit'
			}
		return render(request,'Admin/tag.html',context)
    

def delete_tag(request,num):
	tag=Tag.objects.get(pk=num)
	tag.delete()
	return HttpResponseRedirect('/Admin/tags/')



class Tag_searchResults(ListView):
	model=Tag
	template_name='Admin/tags.html'
	def get_queryset(self):
		query=self.request.GET.get('q')
		object_list=Tag.objects.filter(
			name__icontains=query
		)
		return object_list
	def get_context_data(self,**kwargs):
		data=super().get_context_data(**kwargs)
		data['fields']=Tag.get_model_fields(Tag)
		return data