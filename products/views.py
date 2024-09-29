from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from brands.models import Brand
from app import metrics

from categories.models import Category
from . import models, forms


#class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
class ProductListView(ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    #permission_required = 'brands.view_brand'

    #colocar filtro no site
    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        serie_number = self.request.GET.get('serie_number')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')

        if title:
            queryset = queryset.filter(title__icontains=title)
        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)
        if category:
            queryset = queryset.filter(category_id=category)
        if brand:
            queryset = queryset.filter(brand__id=brand)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_metrics'] = metrics.get_product_metrics()
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        return context





#class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
class ProductCreateView(CreateView):

    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
#    permission_required = 'brands.add_brand'


# class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
class ProductDetailView(DetailView):
     model = models.Product
     template_name = 'product_detail.html'
     
#     permission_required = 'brands.view_brand'


# class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
class ProductUpdateView(UpdateView):
     model = models.Product
     template_name = 'product_update.html'
     form_class = forms.ProductForm
     success_url = reverse_lazy('product_list')
#     permission_required = 'brands.change_brand'


# class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
class ProductDeleteView(DeleteView):
     model = models.Product
     template_name = 'product_delete.html'
     success_url = reverse_lazy('product_list')
#     permission_required = 'brands.delete_brand'


# class BrandCreateListAPIView(generics.ListCreateAPIView):
#     queryset = models.Brand.objects.all()
#     serializer_class = serializers.BrandSerializer

# class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Brand.objects.all()
#     serializer_class = serializers.BrandSerializer