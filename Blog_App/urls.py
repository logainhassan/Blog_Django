from Blog_App import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('table/', views.table),
    path('user/',views.user),
]
