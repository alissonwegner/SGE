from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models
# Create your views here.


class SuppliersListView(ListView):
    model = models.Supplier
    template_name = 'suppliers_list.html'
    context_object_name = 'suppliers'