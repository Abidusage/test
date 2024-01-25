from django import forms
from .models import Postsite, Comment

class PostsiteForm(forms.ModelForm):
    class Meta:
        model = Postsite
        fields = ('title', 'content')

class PostsiteUpdateForm(forms.ModelForm):
    class Meta:
        model = Postsite
        fields = ('title', 'content')

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'add a comment'}))
    class Meta:
        model = Comment
        fields = ('content',)