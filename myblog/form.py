from django import forms
class ContactForm(forms.Form):
	subject = forms.CharField()
	email = forms.EmailFileld(required=False)
	message = forms.CharField()