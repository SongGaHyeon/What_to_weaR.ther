from django import forms

class ContactForm(forms.Form):
  name = forms.CharField(required=True)
  subject = forms.CharField(required=True)
  message = forms.CharField(widget=forms.Textarea)
  from_email = forms.EmailField(required=True)