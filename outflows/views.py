#from rest_framework import generics
#from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from app import metrics
from . import models, forms
#, forms, serializers


#class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class OutflowListView(ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_metrics'] = metrics.get_sales_metrics()
        return context

#class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
class OutflowCreateView(CreateView):

    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')
#    permission_required = 'brands.add_brand'


# class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class OutflowDetailView(DetailView):
     model = models.Outflow
     template_name = 'outflow_detail.html'
     
