from django.shortcuts import render
from Admin.models import *
from django.shortcuts import get_object_or_404
from Blog.forms import *
from django.http import HttpResponse, HttpResponseRedirect
  
# Create your views here.
def allTags():
    tags=Tag.objects.all()
    return tags;

def allCategories():
    categories=Category.objects.all()
    return categories


def allPosts(request) :
    
    tags=allTags()
    cats=allCategories()
    context={
        'cats':cats,
        'tags':tags,
        }
    return render(request,'Blog/allPosts.html',context)   

def PostDetails(request,num):
    post=get_object_or_404(Post,id=num)
    comments=Comment.objects.filter(post=post,reply=None).order_by('id')
    tags=allTags()
    cats=allCategories()
    if request.method=='POST':
        comment_form=CommentForm(request.POST or None)
        if comment_form.is_valid():
            content=request.POST.get('content')
            reply_id=request.POST.get('comment_id')  
            replys_qs=None
            # if reply_id:
            #     replays_qs=Comment.objects.get(id=reply_id)
            #     print(replays_qs)
            comment=Comment.objects.create(post=post,content=content,user_id=2,reply_id=reply_id)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
            # comment_form.save()
    else:
        comment_form= CommentForm()        

    
    context={
        'post':post,
        'comments':comments,
        'commentForm':comment_form,
        'cats':cats,
        'tags':tags
    } 
    return render(request,'Blog/postDetails.html',context)  

def categoryPosts(request,name):
    category=Category.objects.get(Name=name)
    posts=category.posts.all()
    tags=allTags()
    categories=allCategories()
    context={
        'posts':posts,
        'cats':categories,
        'tags':tags
        }
    return render(request,'Blog/cat_tag.html',context)

def tagPosts(request,name):
    tag=Tag.objects.get(name=name)
    posts=tag.posts.all()
    tags=allTags()
    categories=allCategories()
    context={
        'posts':posts,
        'cats':categories,
        'tags':tags
        }
    return render(request,'Blog/cat_tag.html',context)
