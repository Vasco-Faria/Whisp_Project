from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import ImageField

class Post(models.Model):
    text = models.CharField(max_length=240)
    date = models.DateTimeField(auto_now=True)
    #comments = models.ManyToManyField(User, through='Comment', related_name='commented_posts')
    image = ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    
    likes = models.ManyToManyField(User, default=None, blank=True,related_name="liked")

    def __str__(self):
        return self.text
    
    @property
    def num_likes(self):
        return self.liked.all.count()

    def get_comment_count(self):
        return self.comment_set.count() 
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like by {self.user.username} on Post {self.post.id}'
            
    def user_has_liked(self, user):
        return self.objects.filter(user=user, post=self).exists()
    