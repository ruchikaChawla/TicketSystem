import django_tables2 as tables

from ticketApp.models import Ticket


class TicketTable(tables.Table):
    class Meta:
        model = Ticket
