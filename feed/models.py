from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import ImageField

class Post(models.Model):
    text = models.CharField(max_length=240)
    date = models.DateTimeField(auto_now=True)
    image = ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='liked',default=None, blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
   

    def __str__(self):
        return self.text
    
    @property
    def num_likes(self):
        return self.likes.count()

    
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like',max_length=10)

    def __str__(self):
        return str(self.post)  
    
    
class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"comment from {self.author} on {self.post}"
    