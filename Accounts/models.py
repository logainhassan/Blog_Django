# from django.db import models
# from django.contrib.auth.models import ( BaseUserManager,AbstractBaseUser)


# class MyUserManager(BaseUserManager):
# 	def create_user(self,username,email,password=None):
# 		if not email:
# 			raise ValueError('Users must have an email address')

# 		user =self.model(
# 			username=username,
# 			email = self.normalize_email(email)
# 		)
# 		user.set_password(password)
# 		user.save(using=self.db)
# 		return user

# 	def create_superuser(self,username,email,password=None):
# 		user =self.create_user(
# 			username,email,password=password
# 		)
# 		user.role = 0
# 		user.is_staff = True
# 		user.save(using=self.db)
# 		return user


# class MyUser(AbstractBaseUser):
# 	username = models.CharField(max_length=200, unique=True,verbose_name='username')
# 	first_name =  models.CharField(blank=True, max_length=30, verbose_name='first name')
# 	last_name = models.CharField(blank=True, max_length=150, verbose_name='last name')
# 	email = models.EmailField(max_length=254, unique=True,verbose_name='email address')
# 	ROLES = (
# 		(0, 'Super_Admin'),
# 		(1, 'Admin'),
# 		(2, 'User'),
# 	)
# 	role = models.IntegerField(default=2, choices=ROLES,verbose_name='role')
# 	is_active = models.BooleanField(default=True,verbose_name='active status')
# 	avatar = models.ImageField(max_length=500,upload_to='Images/',null=True)
# 	is_staff= models.BooleanField(default=True, verbose_name='staff status')

# 	objects = MyUserManager()

# 	USERNAME_FIELD = 'username'
# 	REQUIRED_FIELDS = ['email']

# 	def __str__(self):
# 		return self.email

# 	def get_short_name(self):
# 		return self.email


# # def has_perm(self,perm,obj=None):
# # 	"Does the user have a specific permission ?"
# # 	return True

# # def has_module_perms(self,app_label):
# # 	"Does the user have a permissions to view the app `app_label` ?"
# # 	return True