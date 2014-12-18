"""
example of using the local flavor app for phone number validation
from django import forms
from localflavor.us.forms import USPhoneNumberField

class SignUpForm(forms.Form):
    phone = USPhoneNumberField()
"""