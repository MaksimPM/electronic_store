from django.urls import path
from django.views.decorators.cache import cache_page, never_cache
from catalog.views import ProductListView, ProductDetailView, CatalogListView, BaseListView, ContactsView, \
    BlogCreateView, BlogListView, BlogUpdateView, BlogDetailView, BlogDeleteView, toggle_activity, \
    ProductCreateView, ProductUpdateView

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('base/', BaseListView.as_view()),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('create/', never_cache(BlogCreateView.as_view()), name='create'),
    path('blog/', BlogListView.as_view(), name='list'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('view/<int:pk>/', cache_page(60)(BlogDetailView.as_view()), name='view'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
    path('product_create/', never_cache(ProductCreateView.as_view()), name='create_product'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
]
