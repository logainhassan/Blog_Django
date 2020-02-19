from Blog_App import views
from django.urls import path

urlpatterns = [
    path('table/', views.table),
    path('table/add_user',views.addUser),
    path('table/edit_user/<num>',views.editUser),
    path('table/delete_user/<num>',views.deleteUser),
]
