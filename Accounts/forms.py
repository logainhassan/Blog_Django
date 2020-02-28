from django.contrib.auth import get_user_model

from django import forms
from django.db.models import Q
from Admin.models import MyUser
from django.utils import timezone


User = get_user_model()	

class UserCreationForm(forms.ModelForm):
	password2 =forms.CharField(label="Password Confirmation",widget=forms.PasswordInput(attrs={'class':'input100','placeholder':'Password Confirmation'}))

	class Meta:
		model = User
		fields =('username','first_name','last_name','email','password')
		widgets = {
			'username' : forms.TextInput(attrs={'class':'input100','placeholder':'UserName'}),
			'first_name' : forms.TextInput(attrs={'class':'input100','placeholder':'FirstName','required':'True'}),
			'last_name' : forms.TextInput(attrs={'class':'input100','placeholder':'LastName','required':'True'}),
			'email' : forms.EmailInput(attrs={'class':'input100','placeholder':'Email'}),
			'password' : forms.PasswordInput(attrs={'class':'input100','placeholder':'Password'}),
		}
	
	def clean_username(self):
		username = self.cleaned_data['username'].lower()
		r = User.objects.filter(username=username)
		if r.count():
			raise  forms.ValidationError("Username already exists")
		return username

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		r = User.objects.filter(email=email)
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


class UserLoginForm(forms.Form):
	query = forms.CharField(label = 'query',widget=forms.TextInput(attrs={'class':'input100','placeholder':'UserName/Email'}))
	password = forms.CharField(label = 'Password',widget=forms.PasswordInput(attrs={'class':'input100','placeholder':'Password'}))

	def clean(self,*args,**kwargs):
		query = self.cleaned_data.get('query')
		password = self.cleaned_data.get('password')
		user_qs_final = User.objects.filter(
				Q(username__iexact=query) |
				Q(email__iexact=query)
			).distinct()
		if not user_qs_final.exists() and user_qs_final.count != 1:
			raise forms.ValidationError("Invalid credentials - user does not exist")
		user_obj = user_qs_final.first()
		if not user_obj.check_password(password):
			raise forms.ValidationError("credentials are not correct")
		if not user_obj.is_active:
			raise forms.ValidationError("sorry you are blocked contact the admin")
		self.cleaned_data["user_obj"] = user_obj
		return super(UserLoginForm, self).clean(*args,**kwargs)





