from django.contrib import admin
from Blog_App.models import Forbidden
from Blog_App.models import Users,Posts

# Register your models here.

class CustomForbidden(admin.ModelAdmin):
    fieldsets = (['Forbidden Words', {'fields': ['word']}],)

    list_display = ['word']
    list_filter = ['word']
    search_fields = ['word']


admin.site.register(Forbidden, CustomForbidden)
admin.site.register(Users)
admin.site.register(Posts)
