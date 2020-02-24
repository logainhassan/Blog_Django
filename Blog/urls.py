from Blog import views
from django.urls import path
urlpatterns=[
   
    path('',views.allPosts),
    path('post/<num>',views.PostDetails),

    
]