from django.db import models


class Ticket(models.Model):
    name = models.CharField(max_length=255, default='')
    phone_no = models.IntegerField(default='')
    email = models.EmailField(max_length=255, default='')
    issue_type = models.CharField(max_length=255, default='')
    status = models.CharField(max_length=255, default='')
    description = models.TextField(default='')


class Comments(models.Model):
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    description = models.TextField(default='')