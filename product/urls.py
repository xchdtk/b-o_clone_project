from django.urls   import path
from django.views  import View

from product.views import ProductView,SubcategoryProductView, ProductDetailView

urlpatterns = [
    path('/product/all/<int:category_id>', ProductView.as_view()),
    path('/product/list/<int:sub_category_id>', SubcategoryProductView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view())
]