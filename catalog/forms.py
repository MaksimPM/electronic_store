from django import forms

from catalog.models import Product, Version


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    danger_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'user')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get('product_name')
        self.check_exceptional_words(self.danger_words, cleaned_data)
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        self.check_exceptional_words(self.danger_words, cleaned_data)
        return cleaned_data

    @staticmethod
    def check_exceptional_words(danger_words, cleaned_data):
        for word in danger_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Запрещенное слово: {word}!')


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
