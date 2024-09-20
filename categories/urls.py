from django.urls import path
from . import views


urlpatterns = [
    path('categories/list/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    #path('brands/create/', views.BrandCreateView.as_view(), name='brand_create'),
    path('categories/<int:pk>/detail/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    #path('api/v1/brands/', views.BrandCreateListAPIView.as_view(), name='brand-create-list-api-view'),
    #path('api/v1/brands/<int:pk>/', views.BrandRetrieveUpdateDestroyAPIView.as_view(), name='brand-detail-api-view'),
]