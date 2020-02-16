from django.urls import path
from Blog_App import views

urlpatterns = [
    path('home', views.home),
]