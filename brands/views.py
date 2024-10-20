#from rest_framework import generics
#from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
#, forms, serializers


#class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class BrandListView(LoginRequiredMixin, ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
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
class BrandCreateView(LoginRequiredMixin, CreateView):

    model = models.Brand
    template_name = 'brand_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brand_list')
#    permission_required = 'brands.add_brand'


# class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class BrandDetailView(LoginRequiredMixin, DetailView):
     model = models.Brand
     template_name = 'brand_detail.html'
     
#     permission_required = 'brands.view_brand'


# class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
class BrandUpdateView(LoginRequiredMixin, UpdateView):
     model = models.Brand
     template_name = 'brand_update.html'
     form_class = forms.BrandForm
     success_url = reverse_lazy('brand_list')
#     permission_required = 'brands.change_brand'


# class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
class BrandDeleteView(LoginRequiredMixin, DeleteView):
     model = models.Brand
     template_name = 'brand_delete.html'
     success_url = reverse_lazy('brand_list')
#     permission_required = 'brands.delete_brand'


# class BrandCreateListAPIView(generics.ListCreateAPIView):
#     queryset = models.Brand.objects.all()
#     serializer_class = serializers.BrandSerializer

# class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Brand.objects.all()
#     serializer_class = serializers.BrandSerializer