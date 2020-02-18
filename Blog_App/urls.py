from django.urls import path
from Blog_App import views

urlpatterns = [
    path('table/', views.table),
    path('user/',views.user),
    path('Forbidden_Words/', views.Forbidden_Words),
    path('Delete_Forbidden_Word/<num>', views.delete_forbidden_word)

]