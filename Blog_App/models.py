from django.db import models


class Users(models.Model):
	userName = models.CharField(max_length =255,unique=True)
	email = models.EmailField(max_length = 255,unique=True)	
	password = models.CharField(max_length = 50)
	is_active = models.BooleanField(default=True)
	ROLES = (
		(0, 'Super_Admin'),
		(1, 'Admin'),
		(2, 'User'),
	)
	role = models.IntegerField(default=2,choices=ROLES)