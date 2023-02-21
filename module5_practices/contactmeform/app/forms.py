from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    user_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, max_length=200)
