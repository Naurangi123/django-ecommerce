from django.urls import path
from . import views

urlpatterns = [
    path('check/',views.checkout,name="checkout"),
    path('order_summery/',views.order_summery,name='summery'),
]
