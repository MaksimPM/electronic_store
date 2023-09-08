from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_list = [
            {'product_name': 'Рис', 'description': 'Компания Мистраль', 'category': 'Крупы', 'price': 80},
            {'product_name': 'Макароны', 'description': 'Макароны по итальянским традициям', 'category': 'Бакалея',
             'price': 140},
            {'product_name': 'Есентуки', 'description': 'Питьевая лечебная вода', 'category': 'Напитки', 'price': 94},
            {'product_name': 'Соль', 'description': 'Соль поваренная', 'category': 'Бакалея', 'price': 40},
            {'product_name': 'Хлеб', 'description': 'Ржаной хлеб', 'category': 'Бакалея', 'price': 25},
            {'product_name': 'Мука', 'description': 'Мука пшеничная', 'category': 'Бакалея', 'price': 80},
        ]

        Product.objects.all().delete()
        product_for_create = []
        for product_item in products_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)
