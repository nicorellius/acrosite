"""
file        :   forms.py
date        :   2013-1220
module      :   contact
classes     :   ContactForm
desription  :   sets form field attributes for contact page
"""

from django import forms

from localflavor.us.forms import USPhoneNumberField


class ContactForm(forms.Form):
    
    name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'name': 'name',
                'placeholder': 'Enter your name'
            }
        )
    )
    
    company = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'name': 'name',
                'placeholder': 'Enter your company'
            }
        )
    )
    
    phone = USPhoneNumberField(
        max_length=12,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control control-label',
                'type': 'text',
                'name': 'phone',
                'placeholder': 'Enter your phone number',
            }
        )
    )
    
    subject = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'name': 'subject',
                'placeholder': 'Enter subject'
            }
        )
    )
    
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': '5',
                'name': 'message',
                'placeholder': 'Enter message'
            }
        )
    )
    
    sender = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'email',
                'name': 'sender',
                'placeholder': 'Enter email'
            }
        )
    )
    
    cc_sender = forms.BooleanField(
        required=False
    )