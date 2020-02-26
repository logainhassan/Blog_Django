from Blog import views
from django.urls import path
urlpatterns=[
   
    path('',views.allPosts),
    path('post/<num>',views.PostDetails),
    path('category/<name>',views.categoryPosts),
    path('tag/<name>',views.tagPosts),
    
    path('category/unsub-category/<num>',views.sub_category),
    path('category/sub-category/<num>',views.sub_category),


    
]