#from rest_framework import generics
#from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from . import models, forms
#, forms, serializers


#class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class CategoryListView(LoginRequiredMixin, ListView):
    model = models.Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
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
class CategoryCreateView(LoginRequiredMixin, CreateView):

    model = models.Category
    template_name = 'category_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')
#    permission_required = 'brands.add_brand'


# class CaregoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class CategoryDetailView(LoginRequiredMixin, DetailView):
     model = models.Category
     template_name = 'category_detail.html'
     
#     permission_required = 'brands.view_brand'


# class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
class CategoryUpdateView(LoginRequiredMixin, UpdateView):
     model = models.Category
     template_name = 'category_update.html'
     form_class = forms.CategoryForm
     success_url = reverse_lazy('category_list')
#     permission_required = 'brands.change_brand'


# class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
class CategoryDeleteView(LoginRequiredMixin, DeleteView):
     model = models.Category
     template_name = 'category_delete.html'
     success_url = reverse_lazy('category_list')
#     permission_required = 'brands.delete_brand'


# class BrandCreateListAPIView(generics.ListCreateAPIView):
#     queryset = models.Brand.objects.all()
#     serializer_class = serializers.BrandSerializer

# class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Brand.objects.all()
#     serializer_class = serializers.BrandSerializer