from django import forms
from dun.models import Category, Post

class QuestionForm(forms.ModelForm) : 
    class Meta : 
        model = Post
        fields = ['title', 'content']

