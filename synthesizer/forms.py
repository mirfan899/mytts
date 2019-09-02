from django import forms
from django.forms import ModelForm

from synthesizer.models import Transcript


class TranscriptForm(ModelForm):

    class Meta:
        model = Transcript
        fields = ['transcript']
