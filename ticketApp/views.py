from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render

from ticketApp.forms import TicketForm, CommentForm
from ticketApp.models import Ticket, Comments
from ticketApp.table import TicketTable


def home(request):
    return render(request, 'base/base.html')


def open_tickets(request):

    raw_data = Ticket.objects.values_list()
    col_names = Ticket.objects.values().__getitem__(0).keys()
    return render(request, 'ticketApp/open_tickets.html', {'raw_data': raw_data, 'col_names': col_names})


def closed_tickets(request):
    raw_data = Ticket.objects.values_list()
    col_names = Ticket.objects.values().__getitem__(0).keys()
    return render(request, 'ticketApp/closed_tickets.html', {'raw_data': raw_data, 'col_names': col_names})


def edit_tickets(request, ticket_id):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('#')
    else:
        form = CommentForm()
    tickets = Ticket.objects.filter(id=ticket_id)
    all_comments = Comments.objects.filter(ticket_id=ticket_id)
    return render(request, 'ticketApp/edit_tickets.html', {'tickets': tickets, 'form': form, 'all_comments': all_comments})


def close_the_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.status = "Closed"
    ticket.closed_date = date.today()
    ticket.save(update_fields=["closed_date", "status"])
    raw_data = Ticket.objects.values_list()
    col_names = Ticket.objects.values().__getitem__(0).keys()
    return render(request, 'ticketApp/closed_tickets.html', {'raw_data': raw_data, 'col_names': col_names})


def create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('#')
    else:
        form = TicketForm()
    return render(request, 'ticketApp/create.html', {'form': form})


