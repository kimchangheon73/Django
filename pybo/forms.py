from django import forms
from pybo.models import *

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']

class AnswernForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']