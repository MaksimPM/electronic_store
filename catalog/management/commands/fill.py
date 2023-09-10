from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        products_list = [
            {'product_name': 'HONOR X7A', 'description': 'Смартфон Honor X7A 4+128GB Titanium Silver (5109AMLU) '
                                                         'оборудован качественной основной камерой с разрешением 50 Мп.'
                                                         ' Это позволяет создавать яркие и детализированные фотографии '
                                                         'пейзажей, архитектурных построек или групповые снимки. '
                                                         'Автофокус позволяет сконцентрировать внимание на объекте '
                                                         'съемки. Повысить яркость снимков в вечернее время можно с '
                                                         'помощью вспышки. Фронтальная камера с разрешением 8 Мп '
                                                         'используется для селфи и звонков в мессенджерах посредством '
                                                         'видеосвязи. Встроенный литиево-полимерный аккумулятор '
                                                         'обеспечивает до 42 ч работы устройства в режиме разговора. '
                                                         'Смартфон Honor X7A 4+128GB Titanium Silver (5109AMLU) '
                                                         'оборудован восьмиядерным процессором и имеет оптимальный '
                                                         'объем ОЗУ. Это обеспечивает плавную работу устройства без '
                                                         'зависаний, быстрое открытие приложений и отклик в играх. '
                                                         'Объем внутренней памяти при необходимости можно увеличить '
                                                         'посредством установки дополнительной карты формата microSD. '
                                                         'Сенсорный экран с IPS-матрицей обеспечивает воспроизведение '
                                                         'детализированного изображения с естественными цветами. Быстро'
                                                         ' разблокировать смартфон помогают сенсор распознавания лица и'
                                                         ' сканер отпечатка пальца.',
             'category': 'Телефоны',
             'price': 150},
            {'product_name': 'iPhone 14 Pro', 'description': 'Смартфон Apple iPhone 14 Pro 128GB Space Black Dual Sim '
                                                             'имеет камеру с тройным модулем, которая отвечает за '
                                                             'качественную'
                                                             'съемку при любом освещении на улице или дома. Для '
                                                             'создания'
                                                             'селфи есть фронтальный объектив. Модель оснащена мощной '
                                                             'начинкой из производительного процессора A16 Bionic и '
                                                             'пятиядерного графического ускорителя для быстрой загрузки'
                                                             'системы и ресурсоемких приложений. За счет встроенной '
                                                             'памяти'
                                                             'значительного объема в устройстве можно хранить '
                                                             'многочисленные'
                                                             'фото и видео.Смартфон Apple iPhone 14 Pro 128GB Space '
                                                             'Black'
                                                             'Dual Sim имеет слот для двух карт nano-SIM. Модель с '
                                                             'влагонепроницаемым корпусом из алюминия, стекла и '
                                                             'керамики'
                                                             'можно применять при любых погодных условиях. За счет '
                                                             'предустановленной операционной системы устройство '
                                                             'оптимально'
                                                             'применять сразу после приобретения. OLED-экран без рамок '
                                                             'обеспечивает качественное отображение картинки во время '
                                                             'просмотра видео без искажения цветов. Сенсорный дисплей '
                                                             'удобен'
                                                             'для регулирования настроек и быстрой активации '
                                                             'приложения.'
                                                             'Смартфон Apple iPhone 14 Pro 128GB Space Black Dual Sim с'
                                                             'модулем Wi-Fi оптимален для доступа в интернет. Адаптер '
                                                             'Bluetooth предназначен для передачи данных на наушники '
                                                             'или'
                                                             'другие совместимые устройства. Сенсор распознавания лица '
                                                             'обеспечивает защиту данных от посторонних. Заряда '
                                                             'литиевой'
                                                             'батареи хватает на длительное функционирование в режиме '
                                                             'автономности. Для подключения к компьютеру в наборе есть '
                                                             'кабель.',
             'category': 'Телефоны',
             'price': 1200},
            {'product_name': 'Samsung Galaxy S23 Ultra', 'description': 'Смартфон Samsung Galaxy S23 Ultra 256GB Black '
                                                                        '(SM-S918B) оснащен восьмиядерным процессором,'
                                                                        'который отвечает за высокую производительность'
                                                                        ' модели в многозадачном режиме. За счет этого'
                                                                        ' эффективно снижен риск возникновения сбоев '
                                                                        'при участии в виртуальных сражениях, '
                                                                        'ретушировании изображений, монтаже видео, '
                                                                        'проведении прямых эфиров и стримов. Дисплей '
                                                                        'Dynamic AMOLED 2X характеризуется широким '
                                                                        'цветовым охватом и высокой плотностью пикселей'
                                                                        '. Это способствует качественному отображению '
                                                                        'ленты социальных сетей, текстовых документов '
                                                                        'и мультимедийных объектов. Благодаря частоте '
                                                                        'обновления 120 Гц обеспечены плавный скроллинг'
                                                                        ' и отсутствие искажений при воспроизведении '
                                                                        'динамичных эпизодов. Основная камера '
                                                                        'оборудована модулем с разрешением 200 МП. '
                                                                        'Благодаря этому обеспечено получение кадров с '
                                                                        'высоким уровнем детализации. За счет различных'
                                                                        ' режимов можно создавать выразительные '
                                                                        'портреты, групповые фото, снимки звездного '
                                                                        'неба и макроизображения независимо от условий '
                                                                        'освещения. Фронтальная камера оптимальна для '
                                                                        'комфортного общения и селфи. Устройство '
                                                                        'поддерживает возможность использования пера '
                                                                        'S Pen. Это способствует комфортному '
                                                                        'рисованию, ведению заметок и управлению '
                                                                        'смартфоном Samsung Galaxy S23 Ultra 256GB '
                                                                        'Black (SM-S918B).',
             'category': 'Телефоны',
             'price': 1050},
            {'product_name': 'Xiaomi Redmi Note 12', 'description': 'Смартфон Xiaomi Redmi Note 12 6+128GB Gray '
                                                                    'изготовлен в форме моноблока. Корпус имеет '
                                                                    'степень защиты IP53, что делает его устойчивым к '
                                                                    'воздействию пыли и влаги. Модель поддерживает '
                                                                    'установку двух Nano-SIM-карт, благодаря чему '
                                                                    'можно пользоваться мобильной связью от разных '
                                                                    'операторов. Устройство поставляется с '
                                                                    'предустановленной ОС Android 13, которая имеет '
                                                                    'простой и понятный пользовательский интерфейс. '
                                                                    'Восьмиядерный процессор Snapdragon 685 и '
                                                                    'оптимальный объем оперативной памяти '
                                                                    'обеспечивают высокую производительность в режиме '
                                                                    'многозадачности. Графический ускоритель Adreno '
                                                                    '610 и частота обновления экрана 120 Гц создают '
                                                                    'комфортные условия при просмотре видеоконтента. '
                                                                    'Объем встроенной памяти 128 ГБ оптимален для '
                                                                    'хранения большого количества личных данных. '
                                                                    'Смартфон Xiaomi Redmi Note 12 6+128GB Gray '
                                                                    'оборудован AMOLED-экраном диагональю 6,'
                                                                    '67 дюйма и разрешением 2400x1080 пикселей. За '
                                                                    'счет этого выводимое изображение характеризуется '
                                                                    'качеством, контрастностью и насыщенностью '
                                                                    'цветов. Для выхода в интернет предназначен '
                                                                    'Wi-Fi-модуль. Bluetooth-адаптер позволяет '
                                                                    'подключать беспроводную гарнитуру. Три основные '
                                                                    'камеры со встроенной вспышкой и автофокусировкой '
                                                                    'позволяют создавать качественные фотографии при '
                                                                    'любом освещении.',
             'category': 'Телефоны',
             'price': 190},
        ]

        Product.objects.all().delete()
        product_for_create = []
        for product_item in products_list:
            product_for_create.append(Product(**product_item))

        Product.objects.bulk_create(product_for_create)
