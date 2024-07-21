from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Product
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
