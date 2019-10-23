from django import forms
from django.forms import ModelForm
from .models import Ticket


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['name',
                  'phone_no',
                  'email',
                  'issue_type',
                  'status',
                  'description']
