from django import forms
from django.forms import ModelForm

from synthesizer.models import Transcript


class TranscriptForm(ModelForm):

    class Meta:
        model = Transcript
        widgets = {
            'transcript': forms.Textarea(attrs={'class': "form-control mb-4", "rows": "4"}),
        }
        fields = ['transcript']
