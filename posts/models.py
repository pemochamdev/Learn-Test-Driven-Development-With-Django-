from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

"""
    class Post
    -id:int
    -title:varchar
    -body:text
    -created_at:datetime
    updated_at:datetime
"""
User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"post_id": self.id})
    
