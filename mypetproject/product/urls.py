from django.urls import path
from .views import ProductListView
from .views import ProductCategoryView

app_name = 'product'

urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('category/<int:category_id>', ProductCategoryView.as_view(), name='category')
]