from django import forms
from .models import Post

class PostForm(forms.ModelForm): #tell Django that this form is a ModelForm
	
	class Meta:
		model = Post
		fields = ('title', 'text', )
