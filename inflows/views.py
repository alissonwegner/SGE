#from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
#, forms, serializers


#class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class InflowListView(LoginRequiredMixin, ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10

    def get_queryset(self):
     queryset = super().get_queryset()
     product = self.request.GET.get('product')
     if product:
         queryset = queryset.filter(product__title__icontains=product)
          #product__title__icontains se utiliza assim por causa do produto. Tem que pesquisar o titulo de dentro do produto
          #ele faz o icontains dentro do product procurando o title
     return queryset


#class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
class InflowCreateView(LoginRequiredMixin, CreateView):

    model = models.Inflow
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')
#    permission_required = 'brands.add_brand'


# class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class InflowDetailView(LoginRequiredMixin, DetailView):
     model = models.Inflow
     template_name = 'inflow_detail.html'
     
