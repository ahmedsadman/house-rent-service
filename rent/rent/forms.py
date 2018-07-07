from django import forms
from posts.models import District, Area


class SearchForm(forms.Form):
    district = forms.ModelChoiceField(queryset=District.objects.all(
    ), widget=forms.Select(attrs={'id': 'district_choice'}))
    area = forms.ModelChoiceField(required=False, queryset=Area.objects.all(
    ), widget=forms.Select(attrs={'id': 'area_choice'}))
    family_allowed = forms.BooleanField(required=False)
    office_allowed = forms.BooleanField(required=False)
    bachelors_allowed = forms.BooleanField(required=False)
