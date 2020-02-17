from django.db import models

# Create your models here.

class User_Post(models.Model):
    id = models.CharField(primary_key=True,max_length=30)
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts,on_delete=models.CASCADE)
    like = models.BooleanField()
    def __init__(self):
        return self.like
    

class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    content = models.TextField(max_length=200)
    reply_id = models.ForeignKey('self',on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE)
    post_id = models.ForeignKey(Posts,on_delete=models.CASCADE)
    def __init__(self):
        return self.id