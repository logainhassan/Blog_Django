from django.urls import path
from Blog_App import views

urlpatterns = [
    path('table/', views.table),
    path('user/',views.user),
    path('Forbidden_Words/', views.Forbidden_Words),
    path('Forbidden_Words/Add_Forbidden_Word', views.add_forbidden_word),
    path('Forbidden_Words/Delete_Forbidden_Word/<num>', views.delete_forbidden_word)
]