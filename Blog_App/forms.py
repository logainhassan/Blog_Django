from django import forms 
from Blog_App.models import Users

class UserForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = ('user_name','email','password','is_active','role')
		widgets = {
		'user_name' : forms.TextInput(attrs={'class':'form-control'}),
		'email' : forms.EmailInput(attrs={'class':'form-control'}),
		'password' : forms.PasswordInput(attrs={'class':'form-control'}),
		'is_active' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
		'role' : forms.Select(attrs={'class':"btn btn-primary dropdown-toggle", 'type':"button" }),
		}
		
