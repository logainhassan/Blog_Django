from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # path('admin-Default/', admin.site.urls),
    path('Admin/', include('Admin.urls')),
    path('', include('Blog.urls')),
    path('Accounts/', include('Accounts.urls')),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
