from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreditCardEntry.as_view())
]
