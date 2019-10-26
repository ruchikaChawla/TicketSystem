from datetime import date, datetime

from django.db import models

ISSUE_CHOICES =[
    ('Technical', 'Technical'),
    ('Billing', 'Billing'),
    ('Service', 'Service'),
]

STATUS_CHOICES =[
    ('Open', 'Open'),
    ('Closed', 'Closed'),
]



class Ticket(models.Model):
    name = models.CharField(max_length=255, default='')
    agent = models.CharField(max_length=255, default='admin')
    phone_no = models.IntegerField(default='')
    email = models.EmailField(max_length=255, default='')
    issue_type = models.CharField(max_length=20, choices=ISSUE_CHOICES)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default='Open')
    description = models.TextField(default='')
    creation_date = models.DateTimeField(default=datetime.now())
    closed_date = models.DateTimeField(blank=True, editable=True, null=True)

class Comments(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    description = models.TextField(default='')
    created_at = models.DateTimeField(default=datetime.now())
    agent = models.CharField(max_length=255, default='admin')
