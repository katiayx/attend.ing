from django import forms

class InputForm(forms.Form):

	keywords = forms.CharField(label='keywords')