from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns=[
    path('',views.products,name="products"),
    path("search/",views.search,name="search"),
    path('add_product/',views.add_product,name="add_product"),
    path('product/<int:id>/', views.product_details, name='product_details'),
    path('product/edit/<int:id>/', views.product_edit, name='product_edit'),
    path('product/add_review/<int:id>/', views.add_review, name='add_review'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/delete/<int:product_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('cart/edit/<int:cart_item_id>/', views.edit_cart, name='edit_cart'),
    path('error/', views.error,name='error'),
    # path('error/', TemplateView.as_view(template_name='products/error.html'), name='error'),

]