from django import forms
from .models import Post


class PostForm(forms.ModelForm):
	class Meta:
		model= Post
		fields = ('title', 'author', 'text')


		widgets = { 
		'title' : forms.TextInput(attrs= {'class': 'form-control'}),
		'author' : forms.Select(attrs= {'class': 'form-control'}),
		'text' : forms.Textarea(attrs= {'class': 'form-control'}), 
		}