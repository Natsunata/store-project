from django.urls import path
from api import views

app_name = 'api'

urlpatterns = [
    path('product-list/', views.ProductListAPIView.as_view(), name='product-list')
]