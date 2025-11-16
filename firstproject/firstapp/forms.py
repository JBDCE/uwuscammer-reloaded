from django.forms import forms, ModelForm
from .models import Reservation

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'first_name',
            'last_name',
            'guest_count',
            'comments',
        ]
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'guest_count': 'How many people are staying over?',
            'comments': 'Other requests?',
        }
        help_texts = {
            'comments': 'This is a test',
        }
