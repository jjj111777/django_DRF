from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create_product'),
    path('', views.list_products, name='list_products'),
    path('<int:productId>/', views.update_product, name='update_product'),
    path('<int:productId>/delete/', views.delete_product, name='delete_product'),
]
