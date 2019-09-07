from django import forms

class ContactForm(forms.Form):
        to =forms.EmailField(required=True, widget = forms.TextInput(attrs={'class':'form-control col-sm-4','placeholder':'Email Address'}))
        subject =forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control col-sm-4', 'placeholder':'subject'}))
        message =forms.CharField(required=True, widget = forms.Textarea(attrs={'class':'form-control col-sm-4','placeholder':'Message'}),label=(''))
