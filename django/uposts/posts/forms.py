from django import forms
from .models import Post

class PostForm(forms.ModelForm):  
    
    class Meta:             #  specified fields of form
        model = Post
        field = ['title', 'image']
        fields='__all__'  ## fix for "Creating a ModelForm without either the 'fields' attribute or the 'exclude' attribute is prohibited"
