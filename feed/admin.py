from django.contrib import admin
from .models import Post,Like

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post,PostAdmin)
admin.site.register(Like)
