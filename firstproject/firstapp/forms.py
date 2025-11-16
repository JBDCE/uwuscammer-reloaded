from django.forms import forms, ModelForm
from .models import Reservation

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'  # This does not feel right...
