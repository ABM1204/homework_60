from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Product, CartItem
from .forms import ProductForm

class CategoryListView(ListView):
    model = Category
    template_name = 'categories_view.html'
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'add_category.html'
    success_url = reverse_lazy('categories_view')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'edit_category.html'
    success_url = reverse_lazy('categories_view')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'delete_category.html'
    success_url = reverse_lazy('categories_view')

class ProductListView(ListView):
    model = Product
    template_name = 'products_view.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Product.objects.filter(remainder__gte=1).order_by('category', 'name')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return queryset

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_view.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add_product.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductForm()
        return context

    def get_success_url(self):
        return reverse_lazy('product_view', kwargs={'pk': self.object.pk})

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'edit_product.html'
    success_url = reverse_lazy('products_view')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('products_view')


class CartView(ListView):
    model = CartItem
    template_name = 'cart_view.html'
    context_object_name = 'cart_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = CartItem.objects.all()
        total = sum(item.product.price * item.quantity for item in cart_items)
        context['total'] = total
        return context

def add_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('products_view')

def remove_from_cart(request, pk):
    cart_item = CartItem.objects.get(pk=pk)
    cart_item.delete()
    return redirect('cart_view')
