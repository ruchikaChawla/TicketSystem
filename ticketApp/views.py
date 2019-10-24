from django.http import HttpResponseRedirect
from django.shortcuts import render

from ticketApp.forms import TicketForm, CommentForm
from ticketApp.models import Ticket
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
    tickets = TicketTable(Ticket.objects.filter(id=ticket_id))
    return render(request, 'ticketApp/edit_tickets.html', {'ticket_id': tickets, 'form': form})


def create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('#')
    else:
        form = TicketForm()
    return render(request, 'ticketApp/create.html', {'form': form})


