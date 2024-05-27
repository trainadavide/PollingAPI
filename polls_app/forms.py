from django import forms
from django.forms import inlineformset_factory as inLineFormSetFactory
from .models import *

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['title']

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['text']

OptionFormSet = inLineFormSetFactory(Poll, Option, form=OptionForm, extra=2, can_delete=True)