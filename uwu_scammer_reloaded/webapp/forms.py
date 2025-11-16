from django.forms import forms, ModelForm
from .models import CreditCard

class CreditCardForm(ModelForm):
    class Meta:
        model = CreditCard
        fields = '__all__'