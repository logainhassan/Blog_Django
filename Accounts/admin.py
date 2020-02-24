from django.contrib import admin

# Register your models here.

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm
from Admin.models import MyUser
# Register your models here.

class UserAdmin(BaseUserAdmin):
	add_form = UserCreationForm

	list_display =['username','email','role']
	list_filter = ['role',]

	fieldsets = (
		(None,{'fields':('username','email','password')}),
		('Permissions', {'fields':('role')})
	)
	search_fields = ('username','email')
	ordering = ('username','email')

	filer_horizontal = {}


admin.site.unregister(Group)