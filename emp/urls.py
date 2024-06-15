from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product),
    path('collections/', views.collection),
    path('products/<slug:slug>', views.product_query),
    path('collections/<slug:slug>', views.collection_query)
]
