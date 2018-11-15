from django import forms

class EmerSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')

