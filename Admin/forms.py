from django import forms 
from Admin.models import *
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()	

class UserCreationForm(forms.ModelForm):
	# password1 =forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'input100','placeholder':'Password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	avatar =forms.ImageField(label='Avatar', required=False, error_messages={'invalid':"Images only"}, widget=forms.FileInput(attrs={'class':'form-control-image'}))
	ROLES = (
      (1, 'Admin'),
      (2, 'User'),
 	)
	role= forms.CharField(label = "role", widget=forms.Select(choices=ROLES,attrs={'class':"btn btn-primary dropdown-toggle", 'type':"button" }))
	
	class Meta:
		model = MyUser
		fields =('username','email','password','is_active','role')
		widgets = {
			'username' : forms.TextInput(attrs={'class':'form-control'}),
			'first_name' : forms.TextInput(attrs={'class':'form-control'}),
			'last_name' : forms.TextInput(attrs={'class':'form-control'}),
			'email' : forms.EmailInput(attrs={'class':'form-control'}),
			'password' : forms.PasswordInput(attrs={'class':'form-control'}),
			'is_active' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
		}
	
	def clean_username(self):
		username = self.cleaned_data['username'].lower()
		r = MyUser.objects.filter(username=username)
		if r.count():
			raise  forms.ValidationError("Username already exists")
		return username

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		r = MyUser.objects.filter(email=email)
		if r.count():
			raise  forms.ValidationError("Email already exists")
		return email

	def clean_password2(self):
		cleaned_data = super(UserCreationForm, self).clean()
		password =cleaned_data.get('password')
		password2 =cleaned_data.get('password2')

		if password and password2 and password != password2:
			 raise forms.ValidationError('Passwords do not match')
		return password2


	def save(self,commit=True):
		user = super(UserCreationForm,self).save(commit)
		user.set_password(self.cleaned_data['password'])
		user.last_login = timezone.now()
		if commit:
			user.save()
		return user


class UserChangeForm(forms.ModelForm):
	avatar =forms.ImageField(label='Avatar', required=False, error_messages={'invalid':"Images only"}, widget=forms.FileInput(attrs={'class':'form-control-image'}))
	ROLES = (
      (1, 'Admin'),
      (2, 'User'),
 	)
	role= forms.CharField(label = "role", widget=forms.Select(choices=ROLES,attrs={'class':"btn btn-primary dropdown-toggle", 'type':"button" }))
	

	class Meta:
		model = MyUser
		fields = ('username','email','first_name','last_name','avatar', 'is_active', 'role')
		widgets = {
			'username' : forms.TextInput(attrs={'class':'form-control'}),
			'first_name' : forms.TextInput(attrs={'class':'form-control'}),
			'last_name' : forms.TextInput(attrs={'class':'form-control'}),
			'email' : forms.EmailInput(attrs={'class':'form-control'}),
			'is_active' : forms.CheckboxInput(attrs={'class':'form-check-input'}),
		}

	def clean_username(self):
		username = self.cleaned_data['username'].lower()
		r = User.objects.filter(username=username)
		if r.count() > 1:
			raise  forms.ValidationError("Username already exists")
		return username

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		r = User.objects.filter(email=email)
		if r.count() > 1:
			raise  forms.ValidationError("Email already exists")
		return email


class Category_form(forms.ModelForm):
	class Meta:
		model=Category
		fields=('Name',)
		widgets={
			'Name':forms.TextInput(attrs={'class' :'form-control'})
		}
class TagForm(forms.ModelForm):
	class Meta:
		model=Tag
		fields=('name',)
		widgets={
			'name':forms.TextInput(attrs={'class':'form-control'})
		}

class ForbiddenForm(forms.ModelForm):
	class Meta:
		model = Forbidden
		fields = ('word',)
		widgets = {
			'word' : forms.TextInput(attrs={'class':'form-control'}),
		}


class PostForm(forms.ModelForm):
	# choices=Post.tag.all()
    
	# tag=forms.MultipleChoiceField(choices=(('s','s'),('s','a')),widget =forms.CheckboxSelectMultiple())
	class Meta:
		model = Post
		fields = ('title','image','content','user','tag','category')
		widgets = {
		'title' : forms.TextInput(attrs={'class':'form-control'}),
		'image' : forms.FileInput(attrs={'class':'form-control-image'}),
		'content' : forms.Textarea(attrs={'class':'form-control'}),
		}
		# tag = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())
