from django.contrib.auth.models import User
from django.db import models
from sorl.thumbnail import ImageField

class Post(models.Model):
    text = models.CharField(max_length=240)
    date = models.DateTimeField(auto_now=True)
<<<<<<< HEAD
=======
    #comments = models.ManyToManyField(User, through='Comment', related_name='commented_posts')
>>>>>>> f38ea6520b891ec4bd6f94d749214a8e5f938035
    image = ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='liked',default=None, blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
<<<<<<< HEAD
   
=======
    
    likes = models.ManyToManyField(User, default=None, blank=True,related_name="liked")
>>>>>>> f38ea6520b891ec4bd6f94d749214a8e5f938035

    def __str__(self):
        return self.text
    
    @property
    def num_likes(self):
        return self.liked.all.count()

    
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='like',max_length=10)

    def __str__(self):
        return str(self.post)            
    
    