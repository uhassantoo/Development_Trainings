from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexPage(TemplateView):
    template_name = 'index.html'
    
class CartPage(TemplateView):
    template_name = 'cart.html'