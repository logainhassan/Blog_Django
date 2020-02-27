from django.shortcuts import render
from Admin.models import *
from django.shortcuts import get_object_or_404
from Blog.forms import *
from django.http import HttpResponse, HttpResponseRedirect
  
# Create your views here.
def allTags():
    tags=Tag.objects.all()
    return tags

def allCategories():
    categories=Category.objects.all()
    return categories


def allPosts(request) :
    recent = recentPosts()
    allposts = posts()
    tags=allTags()
    cats=allCategories()
    context = {
        'recent':recent,
        'allposts':allposts,
        'cats':cats,
        'tags':tags,
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
    if request.method == 'POST':
        comment_form=CommentForm(request.POST or None)
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
            replys_qs=None
            # if reply_id:
            #     replays_qs=Comment.objects.get(id=reply_id)
            #     print(replays_qs)
            comment=Comment.objects.create(post=post,content=new_comment_clear,user_id=1,reply_id=reply_id)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
            # comment_form.save()
        like_form = Likes(request.POST)
        user = MyUser.objects.get(id=1)
        if request.POST.get('like'):
            likeExist = User_Post.objects.filter(user=user,post=post,like=True)
            color = 1
            if likeExist.exists():
                
                likeExist.delete()
            else:
                like = User_Post.objects.create(post=post,user=user,like=True)
                like.save()
        if request.POST.get('dislike'):
            dislikeExist = User_Post.objects.filter(user=user,post=post,like=False)
            if dislikeExist.exists():
                dislikeExist.delete()
            else:
                dislike = User_Post.objects.create(post=post,user=user,like=False)
                dislike.save()
            maxDislikes = User_Post.objects.filter(like = '0').count() 
            if maxDislikes==10:
	            post.delete()
	            return HttpResponseRedirect('')
    else:
        comment_form= CommentForm()        
           

    context={
        'post':post,
        'comments':comments,
        'commentForm':comment_form,
        'cats':cats,
        'tags':tags,
        # 'color':color,
    } 
    return render(request,'Blog/postDetails.html',context)  


def recentPosts():
    all_top = Post.objects.order_by('-date')[:5]
    return all_top
    
def posts():
    posts = Post.objects.all().order_by('-date')
    return posts

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
    print(subs)
    if user :
        print(user.id)
        category.subscribes.remove(user)
    else:
        category.subscribes.add(request.user)   
        category.save()
    print(request.user)
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
    

