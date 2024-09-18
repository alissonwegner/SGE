from django.urls import path
from . import views


urlpatterns = [
    path('caregories/list/', views.CaregoryListView.as_view(), name='caregories_list'),
    path('caregories/create/', views.CaregoryCreateView.as_view(), name='caregories_create'),
    #path('brands/create/', views.BrandCreateView.as_view(), name='brand_create'),
    path('caregories/<int:pk>/detail/', views.CaregoryDetailView.as_view(), name='caregories_detail'),
    path('caregories/<int:pk>/update/', views.CaregoryUpdateView.as_view(), name='caregories_update'),
    path('caregories/<int:pk>/delete/', views.CaregoryDeleteView.as_view(), name='caregories_delete'),

    #path('api/v1/brands/', views.BrandCreateListAPIView.as_view(), name='brand-create-list-api-view'),
    #path('api/v1/brands/<int:pk>/', views.BrandRetrieveUpdateDestroyAPIView.as_view(), name='brand-detail-api-view'),
]