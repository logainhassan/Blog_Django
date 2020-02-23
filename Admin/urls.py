from django.urls import path
from Admin import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # User part
    path('table/', views.table),
    path('user/',views.user),
    path('table/delete_user/<num>',views.deleteUser),
    path('table/add_user',views.addUser),
    path('table/edit_user/<num>',views.editUser),

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
    path('post/<num>',views.post),
]
