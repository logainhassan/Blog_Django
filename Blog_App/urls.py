from Blog_App import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('table/', views.table),
    path('user/',views.user),
    path('category/',views.all_Category),
    path('table/add_user',views.addUser),
    path('table/edit_user/<num>',views.editUser),
    path('category/delete_category/<num>',views.delete_Category),
    path('category/edit_category/<num>',views.edit_Category),
    path('category/add_category',views.add_Category),
    path('category/search/',views.Cat_searchResults.as_view())
]
