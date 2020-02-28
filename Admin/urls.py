from django.urls import path
from Admin import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('users/', views.user),
    # path('user/',views.user),
    path('users/add_user',views.addUser),
    path('users/edit_user/<num>',views.editUser),
    path('users/delete_user/<num>',views.deleteUser),
    path('users/search/',views.userSearch.as_view()),


    # Forbidden_Words part 
    path('Forbidden_Words/', views.Forbidden_Words),
    path('Forbidden_Words/Add_Forbidden_Word', views.add_forbidden_word),
    path('Forbidden_Words/Edit_Forbidden_Word/<num>', views.edit_forbidden_word),
    path('Forbidden_Words/Delete_Forbidden_Word/<num>', views.delete_forbidden_word),
    path('Forbidden_Words/Search_Forbidden_Word', views.Search_forbidden_word),

    # Category part
    path('category/',views.all_Category),
    path('category/delete_category/<num>',views.delete_Category),
    path('category/edit_category/<num>',views.edit_Category),
    path('category/add_category',views.add_Category),
    path('category/search/',views.Cat_searchResults.as_view()),

    # Post part
    path('posts/',views.posts),
    path('add_post/',views.addPost),
    path('edit_post/<num>',views.editPost),
    path('posts/<num>',views.deletePost),
    path('posts/search/',views.PostSearch.as_view()),
    path('post/<num>',views.post),
    path('post_details/<num>', views.view_Post_Details),

    path('tags/',views.tags),
    path('addTag/',views.add_tag),
    path('editTag/<num>',views.edit_tag),
    path('delTag/<num>',views.delete_tag),
    path('tag/search/',views.Tag_searchResults.as_view()),

]
