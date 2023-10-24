from django import forms

class PostForm(forms.Form):
    text = forms.CharField()
    image = forms.ImageField(required=False)
    video = forms.FileField(required=False)