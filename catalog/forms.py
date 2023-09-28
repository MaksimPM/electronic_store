from django import forms

from catalog.models import Product, Version


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'description', 'price', 'product_pic',)

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        danger_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in danger_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Запрещенное слово: {word}!')
            return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        danger_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in danger_words:
            if word in cleaned_data:
                raise forms.ValidationError(f'Запрещенное слово: {word}!')
            return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    def clean_active_version(self):
        active_version = self.cleaned_data.get('active_version')

        if active_version:
            existing_true_objects = Version.objects.filter(active_version=True)

            if self.instance.pk:
                existing_true_objects = existing_true_objects.exclude(pk=self.instance.pk)

            if existing_true_objects.exists():
                raise forms.ValidationError('Активная версия продукта уже существует!')

        return active_version
