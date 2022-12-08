"""Forms of the project."""
from django import forms
from django.core.validators import RegexValidator
from things.models import Thing
# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widget = {'description': forms.Textarea(attrs={'maxlength': 120, 'required': True}),
                  'quantity': forms.NumberInput()}
        exclude = ['created_at']