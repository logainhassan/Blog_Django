from django.shortcuts import render
from Admin.models import *
from django.shortcuts import get_object_or_404
from Blog.forms import *
from django.http import HttpResponse, HttpResponseRedirect

  
from django.views.generic import  ListView
from django.db.models import Q
# Create your views here.
def allTags():
    tags=Tag.objects.all()
    return tags

def allCategories():
    categories=Category.objects.all()
    return categories

def top_posts(request):
    posts = [];
    categories = Category.objects.all()
    cats = []
    for cat in categories:
        subs = cat.subscribes.all()
        user=subs.filter(id=request.user.id).first()
        if user:
            posts += list(cat.posts.all())
            posts.sort(key = lambda a: a.likes,reverse=True)
            posts=list(dict.fromkeys(posts))
   
    if len(posts) >= 3:
        # print(posts[0].title)
        return posts[:3] 
    else:
        all_top = Post.objects.order_by('-likes')[:3]
        return all_top

def allPosts(request) :
    recent = recentPosts(request)
    allposts = posts(request)
    tags=allTags()
    cats=allCategories()
    tops = top_posts(request)
    context = {
        'recent':recent,
        'allposts':allposts,
        'cats':cats,
        'tags':tags,
        'tops':tops
        }
    return render(request,'Blog/allPosts.html',context)

def PostDetails(request, num):
    bad_list = []
    forbidden_words = Forbidden.objects.all()
    for bad_word in forbidden_words:
        bad_list.append(bad_word.word)

    post=get_object_or_404(Post,id=num)
    comments = Comment.objects.filter(post=post,reply=None).order_by('id')
    tags = allTags()
    cats = allCategories()
    
    # color=0
    # dicolor=0
    like_form = Likes(request.POST)

    user = MyUser.objects.get(id=request.user.id)
    if request.method == 'POST':
        comment_form=CommentForm(request.POST or None,request.FILES or None)

        if comment_form.is_valid():
            content=request.POST.get('content')
            new_comment = []
            comment_words = content.split(" ")
            for word in comment_words:
                if word in bad_list:
                    word = len(word) * "*"

                new_comment.append(word)

            new_comment_clear = ' '.join(map(str, new_comment))

            reply_id=request.POST.get('comment_id')  
            
            
            comment=Comment.objects.create(post=post,content=new_comment_clear,user_id=request.user.id,reply_id=reply_id)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
            # comment_form.save()
        
        if request.POST.get('like'):
            likeExist = User_Post.objects.filter(user=user,post=post,like=True)
            if likeExist.exists():
                likeExist.delete()
                # color=0
            else:
                # color=1
                like = User_Post.objects.create(post=post,user=user,like=True)
                like.save()
                post.likes+=1
                post.save()
        elif request.POST.get('dislike'):
            dislikeExist = User_Post.objects.filter(user=user,post=post,like=False)
            
            if dislikeExist.exists():
                dislikeExist.delete()
                # dicolor = 0
            else:
                # dicolor = 1
                dislike = User_Post.objects.create(post=post,user=user,like=False)
                dislike.save()
                post.likes-=1
                post.save()
            maxDislikes = User_Post.objects.filter(like = '0').count() 
            if maxDislikes==10:
	            post.delete()
	            return HttpResponseRedirect('')
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form= CommentForm()        
           
    likeCounter = User_Post.objects.filter(post=post,like='1').count()
    dislikeCounter = User_Post.objects.filter(post=post,like='0').count()
    flag = User_Post.objects.filter(post=post,user=request.user).first()
    if flag:
        if flag.like==True:
            print(flag)
            flag=1
        else:
            flag=-1
    else:
        flag=0     
    context={
        'post':post,
        'comments':comments,
        'commentForm':comment_form,
        'cats':cats,
        'tags':tags,
        'flag':flag,
        'likeCounter':likeCounter,
        'dislikeCounter':dislikeCounter
    } 
    return render(request,'Blog/postDetails.html',context)  

# all posts >>cats >>user
def recentPosts(request):
    posts = [];
    categories = Category.objects.all()
    cats = []
    for cat in categories:
        subs = cat.subscribes.all()
        user=subs.filter(id=request.user.id).first()
        if user:
            posts += list(cat.posts.all())
            posts.sort(key = lambda a: a.date,reverse=True)
            posts=list(dict.fromkeys(posts))
   
    if posts:
        # print(posts[0].title)
        return posts[:4] 
    else:
        all_top = Post.objects.order_by('-date')[:4]
        return all_top
    # s=Post.objects.filter(category = cats)
    # print(s)
# def com_items(a,b):
#     if a.date > b.date:
#         return 1
#     else :
#         return 0   
def posts(request):
    posts = [];
    categories = Category.objects.all()
    cats = []
    for cat in categories:
        subs = cat.subscribes.all()
        user=subs.filter(id=request.user.id).first()
        if user:
            posts += list(cat.posts.all())
            posts.sort(key = lambda a: a.date,reverse=True)
            posts=list(dict.fromkeys(posts))
   
    if posts:
        # print(posts[0].title)
        return posts
    else:
        posts = Post.objects.all().order_by('-date')
        return posts

# class PostSearch(ListView):
# 	model = Post
# 	template_name = 'Blog/search_result.html'
# 	def get_queryset(self):
# 		query=self.request.GET.get('q')
# 		object_list = Post.objects.filter(
# 			Q(title__icontains=query) | Q(content__icontains=query)
# 		)
#         # context = {'object_list':object_list}
# 		return object_list

def search_posts(request):
    template = 'Blog/search_result.html'
    query = request.GET.get('q')
    object_list = Post.objects.filter(
			Q(title__icontains=query) | Q(content__icontains=query)
		)
    tags = allTags()
    cats = allCategories()

    context = {
        'object_list': object_list,
        'tags' : tags,
        'cats' : cats,
    }

    return render(request, template, context)

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


def sub_category(request,num):
    category=Category.objects.get(id=num)
    subs=category.subscribes.all()
    user=subs.filter(id=request.user.id).first()
    # print(user)
    # print(subs)
    if user :
        # print(user.id)
        category.subscribes.remove(user)
    else:
        category.subscribes.add(request.user)   
        category.save()
    # print(request.user)
    return HttpResponseRedirect("/")
# def like(request,num):  
#     post=get_object_or_404(Post,id=num)
#     if request.method == 'POST':
#         like_form = Likes(request.POST)
#         if request.POST.get('like'):
#             like = User_Post.objects.create(post=num,user=1,like=True)
#             like.save()
#     return HttpResponseRedirect(post.get_absolute_url())
        # elif request.POST.get('dislike'):
        #     User_Post.like = False
    
def about(request):
    # users=MyUser.objects.get(role=0)
    users=MyUser.objects.filter(role=0)
    tags=allTags()
    categories=allCategories()

    context={
        'users':users,
        'cats':categories,
        'tags':tags
    }
    return render(request,'Blog/about.html',context)

def profile(request):
    tags=allTags()
    categories=allCategories()
    user=request.user
    context={
        'cats':categories,
        'tags':tags,
        'user':user
    }
    return render(request,'Blog/profile.html',context)
    
