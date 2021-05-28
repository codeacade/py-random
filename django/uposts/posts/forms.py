from django import forms
from .models import Post

class PostForm(forms.ModelForm):  
    
    class Meta:             #  specified fields of form
        model = Post
        field = ['title', 'image']
