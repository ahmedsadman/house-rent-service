from django import forms
from posts.models import Post, District, Area, Images


class PostForm(forms.ModelForm):
    district = forms.ModelChoiceField(queryset=District.objects.all(
    ), widget=forms.Select(attrs={'id': 'district_choice'}))

    area = forms.ModelChoiceField(queryset=Area.objects.all(
    ), widget=forms.Select(attrs={'id': 'area_choice'}))

    class Meta():
        model = Post
        fields = ('house_name', 'district', 'area', 'house_size', 'address', 'description',
                  'family_allowed', 'office_allowed', 'bachelors_allowed')


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta():
        model = Images
        fields = ('image',)