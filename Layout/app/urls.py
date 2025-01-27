from django.urls import path
from .views import IndexPage , CartPage

urlpatterns = [
    path('', IndexPage.as_view(), name= 'index'),
    path('cart/', CartPage.as_view(), name= 'cart')
]
