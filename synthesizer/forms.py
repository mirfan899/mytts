from django import forms


class TranscriptForm(forms.Form):
    transcript = forms.CharField(widget=forms.Textarea)
