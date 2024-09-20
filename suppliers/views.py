#from rest_framework import generics
#from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
#, forms, serializers


#class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class SupplierListView(ListView):
    model = models.Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 5
    #permission_required = 'brands.view_brand'

    #colocar filtro no site
    def get_queryset(self):
     queryset = super().get_queryset()
     name = self.request.GET.get('name')
     if name:
         queryset = queryset.filter(name__icontains=name)
     return queryset


#class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
class SupplierCreateView(CreateView):

    model = models.Supplier
    template_name = 'supplier_create.html'
    form_class = forms.SupplierForm
    success_url = reverse_lazy('supplier_list')
#    permission_required = 'brands.add_brand'


# class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class SupplierDetailView(DetailView):
     model = models.Supplier
     template_name = 'supplier_detail.html'
     
#     permission_required = 'brands.view_brand'


# class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
class SupplierUpdateView(UpdateView):
     model = models.Supplier
     template_name = 'supplier_update.html'
     form_class = forms.SupplierForm
     success_url = reverse_lazy('supplier_list')
#     permission_required = 'brands.change_brand'


# class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
class SupplierDeleteView(DeleteView):
     model = models.Supplier
     template_name = 'supplier_delete.html'
     success_url = reverse_lazy('supplier_list')
#     permission_required = 'brands.delete_brand'


# class BrandCreateListAPIView(generics.ListCreateAPIView):
#     queryset = models.Brand.objects.all()
#     serializer_class = serializers.BrandSerializer

# class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Brand.objects.all()
#     serializer_class = serializers.BrandSerializer