from django.contrib import admin
from .models import *



class CustomForbidden(admin.ModelAdmin):
    fieldsets = (['Forbidden Words', {'fields': ['word']}],)
    list_display = ['word']
    list_filter = ['word']
    search_fields = ['word']


# Register your models here.

admin.site.register(Forbidden, CustomForbidden)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Post)
