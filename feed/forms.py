from django import forms
from .models import Comment

class PostForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 1,
            'placeholder': '    What are you thinking?',
            'style': 'border: 1px solid #000; border-radius: 5px;margin-top: 1rem;'
        })
    )
    image = forms.ImageField(required=False)
    video = forms.FileField(required=False)
    
    
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=255, required=False)
