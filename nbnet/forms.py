from django.forms import ModelForm

from .models import Movement


class MovementForm(ModelForm):
    class Meta:
        model = Movement
        fields = ('account', 'date', 'description', 'amount')
