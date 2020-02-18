from Blog_App import views
from django.urls import path

urlpatterns = [
    path('table/', views.table),
    path('user/',views.user),
]
