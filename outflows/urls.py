from django.urls import path
from . import views


urlpatterns = [
    path('outflows/list/', views.OutflowListView.as_view(), name='outlow_list'),
    path('outlows/create/', views.OutflowCreateView.as_view(), name='outlow_create'),
    path('outlows/<int:pk>/detail/', views.OutflowDetailView.as_view(), name='outlow_detail'),

    #path('api/v1/brands/', views.BrandCreateListAPIView.as_view(), name='brand-create-list-api-view'),
    #path('api/v1/brands/<int:pk>/', views.BrandRetrieveUpdateDestroyAPIView.as_view(), name='brand-detail-api-view'),
]