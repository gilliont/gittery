from django import forms
from django.core import validators
from .models import Page

def check_for_z(value):
    if str(value[0]).lower() != 'z':
        raise forms.ValidationError("Name needs to start with 'z' ")



class FormCategory(forms.Form):
    name = forms.CharField(max_length=264,
                           validators=[check_for_z])
    views = forms.IntegerField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])


class FormPage(forms.ModelForm):

    class Meta:
        model = Page
        fields = '__all__'