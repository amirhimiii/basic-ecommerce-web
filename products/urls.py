from django.urls import path
from .views import *



feedback
urlpatterns = [
    path('',ProductListView.as_view(),name='product-list'), 
    path('<int:pk>/',product_detail_view,name='product-detail'), 
    path('contact-us/',ContactView.as_view(),name='contact-us'), 
    path('feedback/',feedback,name='feedback'), 
    path('checkout/',ChekoutView.as_view(),name='checkout'), 
    
    path('<int:pk>/update/',ProductUpdateView.as_view(),name='update'), 
    path('<int:pk>/delete/',ProductDeleteView.as_view(),name='product-delete'), 
    path('create/',ProductCreateView.as_view(),name='product-create'), 
     
    path('order-summary/',OrderSummery.as_view(),name='order-summary'),
    path('<int:pk>/add-to-cart/',add_to_cart,name='add-to-cart'), 
    path('<int:pk>/remove-from-cart/',remove_from_cart,name='remove-from-cart'),     
    path('<int:pk>/remove-single-item-from-cart/',remove_single_item_from_cart,name='remove-single-item-from-cart'),     
]
