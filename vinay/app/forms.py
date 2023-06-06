# myapp/forms.py
from django import forms

class PoemSubmissionForm(forms.Form):
    Title_of_your_poem = forms.CharField(max_length=100)
    Your_goodname = forms.CharField(max_length=100)
    The_Poem = forms.CharField(widget=forms.Textarea)