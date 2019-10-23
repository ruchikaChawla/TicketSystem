"""CallHubTicketSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from ticketApp import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ticket/', views.home),
    path('ticket/create/', views.create, name='create'),
    path('ticket/open/', views.open_tickets, name='open'),
    path('ticket/closed/', views.closed_tickets, name='closed'),
    path('ticket/open/edit/<int:ticket_id>/', views.edit_tickets, name='edit'),

]
