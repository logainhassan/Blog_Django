from django.db import models
import datetime


# Create your models here.

class Forbidden(models.Model):
    word = models.CharField(max_length=100)


class Category(models.Model):
    Name = models.CharField(max_length=100)
    def get_model_fields(self):
        return self._meta.fields


class User(models.Model):
    # user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    ROLES = (
        (0, 'Super_Admin'),
        (1, 'Admin'),
        (2, 'User'),
    )
    role = models.IntegerField(default=2, choices=ROLES)


class Post(models.Model):
    # post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Images/')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class User_Post(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField()

    # def __init__(self):
    #     return self.like


class Comment(models.Model):
    # id = models.IntegerField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=200)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)


# class User_Category(models.Model):
#     User_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     Category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    # def __init__(self):
    #     return self.id


# class Post_Category(models.Model):
# 	post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
# 	Category_id = models.ForeignKey(Category, on_delete=models.CASCADE)