from django.views.generic import(ListView)
from .models import Message

# Create your views here.
class HomePage(ListView):
    model = Message
    template_name = 'home.html'