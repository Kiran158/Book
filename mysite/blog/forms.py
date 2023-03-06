from django import forms
from blog.models import Post


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['book', 'author', 'status', 'content']