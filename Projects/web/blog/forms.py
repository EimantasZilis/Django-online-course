from django import forms
from blog.models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("author", "title", "text")

        # Connect specific widgets with CSS classes.
        # Define which fields are associated with which CSS classes.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.TextArea(attrs={
                'class': 'editable medium-editor-textarea postcontent'
                })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("author", "text")

        widgets = {
            "author": forms.TextInput(attrs={"class": "textinputclass"}),
            "text": forms.TextArea(attrs={
                'class': 'editable medium-editor-textarea'
                })
        }


