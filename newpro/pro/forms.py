from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Hostname', max_length=100)
    your_package = forms.CharField(label='Package Name', max_length=100) 
