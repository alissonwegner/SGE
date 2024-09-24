#from rest_framework import generics
#from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
#, forms, serializers


#class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class OutowListView(ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflow'
    paginate_by = 5
    #permission_required = 'brands.view_brand'

    #colocar filtro no site
    def get_queryset(self):
     queryset = super().get_queryset()
     product = self.request.GET.get('product')
     if product:
         queryset = queryset.filter(product__title__icontains=product)
          #product__title__icontains se utiliza assim por causa do produto. Tem que pesquisar o titulo de dentro do produto
          #ele faz o icontains dentro do product procurando o title
     return queryset


#class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
class OutflowCreateView(CreateView):

    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.Outflow
    success_url = reverse_lazy('outflow_list')
#    permission_required = 'brands.add_brand'


# class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class OutflowDetailView(DetailView):
     model = models.Outflow
     template_name = 'outflow_detail.html'
     
