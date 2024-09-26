from django.contrib import admin
from django.urls import path, include
#from django.contrib.auth import views as auth_views
#from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

   # path('api/v1/', include('authentication.urls')),
    path('', include('suppliers.urls')),
    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('products.urls')),
    path('', include('inflows.urls')),
    path('', include('outflows.urls')),
]