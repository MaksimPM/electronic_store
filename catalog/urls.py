from django.urls import path
from catalog.views import ProductListView, ProductDetailView, CatalogListView, BaseListView, ContactsView, \
    BlogCreateView, BlogListView, BlogUpdateView, BlogDetailView, BlogDeleteView, toggle_activity

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('base/', BaseListView.as_view()),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', CatalogListView.as_view(), name='catalog'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('blog/', BlogListView.as_view(), name='list'),
    path('update/<int:pk>', BlogUpdateView.as_view(), name='update'),
    path('view/<int:pk>', BlogDetailView.as_view(), name='view'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
    path('activity/<int:pk>', toggle_activity, name='toggle_activity'),
]
