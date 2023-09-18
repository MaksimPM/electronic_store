from django.shortcuts import get_object_or_404, redirect
from pytils.translit import slugify
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Contacts, Blog


class ProductListView(ListView):
    model = Product
    template_name = "catalog/index.html"


class BaseListView(ListView):
    model = Product
    template_name = "catalog/base.html"


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            email = self.request.POST.get('email')
            message = self.request.POST.get('message')
            print(f'You have new message from {name}({email}): {message}')
        context_data['object_list'] = Contacts.objects.all()
        return context_data


class CatalogListView(ListView):
    model = Product
    template_name = "catalog/products_list.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/products_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = {
            'object': Product.objects.get(pk=self.kwargs.get('pk'))
        }

        return context_data


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview',)
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        if form.is_valid():
            new_content = form.save()
            new_content.slug = slugify(new_content.title)
            new_content.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview',)

    def form_valid(self, form):
        if form.is_valid():
            new_content = form.save()
            new_content.slug = slugify(new_content.title)
            new_content.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('list')


def toggle_activity(pk):
    student_item = get_object_or_404(Blog, pk=pk)
    student_item.is_published = False if student_item.is_published else True

    student_item.save()
    return redirect(reverse('list'))
