from django import forms
from posts.models import Post

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('house_name', 'house_size', 'family_allowed', 'office_allowed', 'bachelors_allowed')