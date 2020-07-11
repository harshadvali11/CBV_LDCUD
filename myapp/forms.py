from django import forms

class DemoForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=18,max_value=100)
    address=forms.CharField(max_length=200,widget=forms.Textarea)

