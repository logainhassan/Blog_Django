from django.db import models

# Create your models here.
class Category(models.Model):
    Name=models.CharField(max_length=200)

class Users(models.Model):
	user_id = models.AutoField(primary_key=True)
	user_name = models.CharField(max_length =255,unique=True)
	email = models.EmailField(max_length = 255,unique=True)	
	password = models.CharField(max_length = 50)
	is_active = models.BooleanField(default=True)
	ROLES = (
		(0, 'Super_Admin'),
		(1, 'Admin'),
		(2, 'User'),
	)
	role = models.IntegerField(default=2,choices=ROLES)

class Posts(models.Model):
	post_id = models.AutoField(primary_key=True)
	title = models.CharField(max_length = 200)
	image = models.ImageField(upload_to ='Images/')
	content = models.TextField()
	date = models.DateTimeField()
	user_id = models.ForeignKey(Users,on_delete=models.CASCADE)


