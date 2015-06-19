from django import forms
from django.core.validators import validate_email


class ContactForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.CharField(label='email', max_length=100, validators=[validate_email])
    subject = forms.CharField(label='subject', widget=forms.Textarea)


class EnquiryForm(forms.Form):
    name = forms.CharField(label='name', max_length=100, widget=forms.TextInput(attrs={'class':'here','placeholder':'Name'}))
    email = forms.CharField(label='email', max_length=100, widget=forms.TextInput(attrs={'class':'here','placeholder':'Email'}))
    contact = forms.CharField(label='contact', max_length=100, widget=forms.TextInput(attrs={'class':'here','placeholder':'Contact'}))
    query = forms.CharField(label='query', max_length=100, widget=forms.TextInput(attrs={'class':'here','placeholder':'Query'}))


class contactform(forms.Form):
    smallname = forms.CharField(label='name', max_length=100)
    smallemail = forms.CharField(label='email', max_length=100, validators=[validate_email])
    subject = forms.CharField(label='subject', widget=forms.Textarea)
