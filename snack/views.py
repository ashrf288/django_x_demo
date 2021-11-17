from django.db.models import fields
from django.shortcuts import render
from django.views.generic import (ListView , DetailView, CreateView , UpdateView ,DeleteView)

# Create your views here.
from .models import Snack
from django.urls import reverse_lazy

class SnackListView(ListView):
    template_name='snack/list_view.html'
    model=Snack


class SnackDetailView (DetailView):
    template_name='snack/snack_details.html'
    model=Snack
    context_object_name='snack'



class SnackCreateView (CreateView):
    template_name='snack/create_snack.html'
    model=Snack
    fields=['title' ,'purchaser', 'description']



class SnackUpdateView (UpdateView):
    template_name='snack/snack_update.html'
    model=Snack
    fields=['title' ,'purchaser', 'description']


class SnackDeleteView (DeleteView):
    template_name='snack/snack_delete.html'
    model=Snack
    success_url = reverse_lazy("home")