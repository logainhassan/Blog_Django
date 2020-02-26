from django.db import models
import datetime
from django.contrib.auth.models import ( BaseUserManager,AbstractBaseUser)
from django.core.validators import RegexValidator

PASSWORD_REGEX = '^(?=.*[0-9]+.*)(?=.*[a-zA-Z]+.*)[0-9a-zA-Z]{6,}$'

class MyUserManager(BaseUserManager):
  def create_user(self,username,email,password=None):
      if not email:
          raise ValueError('Users must have an email address')

      user =self.model(
          username=username,
          email = self.normalize_email(email)
      )
      user.set_password(password)
      user.save(using=self.db)
      return user

  def create_superuser(self,username,email,password=None):
      user =self.create_user(
          username,email,password=password
      )
      user.role = 0
      user.save(using=self.db)
      return user


class MyUser(AbstractBaseUser):
  username = models.CharField(max_length=200, unique=True,verbose_name='username')
  first_name =  models.CharField(blank=True, max_length=30, verbose_name='first name')
  last_name = models.CharField(blank=True, max_length=150, verbose_name='last name')
  email = models.EmailField(max_length=254, unique=True,verbose_name='email address')
  password = models.CharField(max_length=100,validators=[RegexValidator(regex=PASSWORD_REGEX,
        message="Password must contain at least one letter, at least one number, and be longer than eight charaters."
        ,code="invalid_password")],)
  ROLES = (
      (0, 'Super_Admin'),
      (1, 'Admin'),
      (2, 'User'),
  )
  role = models.IntegerField(default=2, choices=ROLES,verbose_name='role')
  is_active = models.BooleanField(default=True,verbose_name='active status')
  avatar = models.ImageField(max_length=500,upload_to='Images/',null=True)
  is_staff= models.BooleanField(default=True, verbose_name='staff status')

  objects = MyUserManager()

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email']

  def __str__(self):
      return self.email

  def get_short_name(self):
      return self.email


# def has_perm(self,perm,obj=None):
#     "Does the user have a specific permission ?"
#     return True

# def has_module_perms(self,app_label):
#     "Does the user have a permissions to view the app `app_label` ?"
#     return True

class Forbidden(models.Model):
    word = models.CharField(max_length=100)
    def __str__(self):
        return self.word
    


class Category(models.Model):
    Name = models.CharField(max_length=100)
    def get_model_fields(self):
        return self._meta.fields
    def __str__(self):
        return self.Name
    


# class User(models.Model):
#     # user_id = models.AutoField(primary_key=True)
#     user_name = models.CharField(max_length=100, unique=True)
#     email = models.EmailField(max_length=100, unique=True)
#     password = models.CharField(max_length=100)
#     is_active = models.BooleanField(default=True)
#     ROLES = (
#         (0, 'Super_Admin'),
#         (1, 'Admin'),
#         (2, 'User'),
#     )
#     role = models.IntegerField(default=2, choices=ROLES)
#     image = models.ImageField(upload_to='Users/',max_length=500,default=None)


class Tag(models.Model):
    name=models.CharField(max_length=100)
    def get_model_fields(self):
        return self._meta.fields
    def __str__(self):
        return self.name
    

class Post(models.Model):
    # post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Posts/',max_length=500)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    tag=models.ManyToManyField(Tag,related_name="posts")
    category=models.ManyToManyField(Category,related_name='posts')

    def __str__(self):
        return '{}{}'.format(self.title,str(self.user.user_name))
    def get_absolute_url(self):
        return "/post/%i" % self.pk


class User_Post(models.Model):
    #id = models.CharField(primary_key=True, max_length=30, auto_created=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField()

    # def __init__(self):
    #     return self.like


class Comment(models.Model):
    # id = models.IntegerField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=200)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True , blank=True, related_name='replies')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,default=0, on_delete=models.CASCADE)
    def __str__(self):
        return '{} : {}'.format(self.content,str(self.date))
    # post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)






# class User_Category(models.Model):
#     User_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     Category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    # def __init__(self):
    #     return self.id


# class Post_Category(models.Model):
# 	post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
# 	Category_id = models.ForeignKey(Category, on_delete=models.CASCADE)