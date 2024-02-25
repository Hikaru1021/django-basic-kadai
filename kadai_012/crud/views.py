from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .models import Product
from django.urls import reverse_lazy

class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    model = Product

class ProductDetailView(DetailView):
    model = Product
    temlpate_name = "crud/product_detail.html"

class ProductCreateView(CreateView):
     model = Product
     fields = '__all__'

class ProductUpdateView(UpdateView):
     model = Product
     fields = '__all__'
     template_name_suffix = '_update_form'

class ProductDeleteView(DeleteView):
     model = Product
     success_url = reverse_lazy('list')
