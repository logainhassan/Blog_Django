from django import forms 
from Blog_App.models import Users ,Category


class UserForm(forms.ModelForm):
	confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	class Meta:
		model = Users
		fields = ('user_name','email','password','confirm_password','is_active','role')
		widgets = {
		'user_name' : forms.TextInput(attrs={'class':'form-control'}),
		'email' : forms.EmailInput(attrs={'class':'form-control'}),
		'password' : forms.PasswordInput(attrs={'class':'form-control'}),
		# 'confirm_password':forms.PasswordInput(attrs={'class':'form-control'}),
		'is_active' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
		'role' : forms.Select(attrs={'class':"btn btn-primary dropdown-toggle", 'type':"button" }),
		}

	def clean(self):
	    cleaned_data = super(UserForm, self).clean()
	    password = cleaned_data.get("password")
	    confirm_password = cleaned_data.get("confirm_password")
	    if password and confirm_password:
	    	if password != confirm_password:
	    		raise forms.ValidationError("The two password fields must match.")
	    return cleaned_data
	
class Category_form(forms.ModelForm):
	class Meta:
		model=Category
		fields=('Name',)
		widgets={
		'Name':forms.TextInput(attrs={'class' :'form-control'})
		}