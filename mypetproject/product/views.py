from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from .models import Product
from .models import ProductCategory


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    queryset = Product.objects.select_related('category').all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cur_category_pk"] = None
        context["categories"] = ProductCategory.objects.all()
        return context


class ProductCategoryView(ProductListView):
    def get_queryset(self):
        category = get_object_or_404(ProductCategory, pk=self.kwargs['category_id'])
        return super().get_queryset().filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cur_category_pk"] = self.kwargs['category_id']
        return context

    