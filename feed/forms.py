from django import forms
from .models import Comment

class PostForm(forms.Form):
    text = forms.CharField()
    image = forms.ImageField(required=False)
    video = forms.FileField(required=False)
    
    
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
