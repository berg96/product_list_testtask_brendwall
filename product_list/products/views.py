from django.views.generic import ListView, CreateView

from .forms import ProductForm
from .models import Product


class ProductListView(ListView):
    model = Product
    paginate_by = 20
    ordering = 'name'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = 'list'
