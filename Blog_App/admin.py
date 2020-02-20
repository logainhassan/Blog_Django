from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)


# Register your models here.

class CustomForbidden(admin.ModelAdmin):
    fieldsets = (['Forbidden Words', {'fields': ['word']}],)

    list_display = ['word']
    list_filter = ['word']
    search_fields = ['word']


admin.site.register(Forbidden, CustomForbidden)
admin.site.register(Users)
admin.site.register(Posts)
