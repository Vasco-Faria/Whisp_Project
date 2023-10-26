from django.contrib import admin
from .models import Post,Like,Comment

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post,PostAdmin)
admin.site.register(Like)





class CommentAdmin(admin.ModelAdmin):
    list_display=('author','post')
    date_hierarchy='date'
    

admin.site.register(Comment,CommentAdmin)