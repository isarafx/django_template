from django import forms
from .models import ContactUs
from django.template.defaultfilters import slugify

class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = '__all__'
        labels = {
            'name':'ชื่อ'
        }
        widgets ={
            'name':forms.DateInput(attrs={'class':'form-control contact-field',  'placeholder':"Your Name"}),
            'cont_email':forms.EmailInput(attrs={'class':'form-control contact-field',  'placeholder':"Your Email"}),
            'subject':forms.DateInput(attrs={'class':'form-control contact-field',  'placeholder':"Subject"}),
            'message':forms.Textarea(attrs={'class':'form-control contact-field',  'placeholder':"Message", 'rows':'8'}),
        }