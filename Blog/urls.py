from Blog import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
   
    path('',views.allPosts),
    path('post/<num>',views.PostDetails),
    path('category/<name>',views.categoryPosts),
    path('tag/<name>',views.tagPosts),
    
    path('category/unsub-category/<num>',views.sub_category),
    path('category/sub-category/<num>',views.sub_category),

    path('about',views.about),
    path('profile',views.profile),
    path('ps/search',views.search_posts),

    # path('',views.PostSearch.as_view()),
    
]