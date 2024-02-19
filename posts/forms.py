from django import forms

from posts.models import Post

class PostCreationForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ('title', 'body')
        