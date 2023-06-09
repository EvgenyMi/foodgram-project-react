import csv

from django.core.management.base import BaseCommand

from ingredients.models import Ingredient


class Command(BaseCommand):
    help = 'Импорт данных из .csv в модель Ingredient'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str, help='Путь к файлу')

    def handle(self, *args, **options):
        print('Начат импорт данных из .csv файла в модель Ingredient.')
        file_path = options.get('path') + 'ingredients.csv'

        if not options['path']:
            print('Не указан путь к файлу!')
            return

        with open(file_path, 'r', encoding='utf-8-sig') as csv_file:
            reader = csv.reader(csv_file)

            for row in reader:
                try:
                    obj, created = Ingredient.objects.get_or_create(
                        name=row[0],
                        measurement_unit=row[1],
                    )
                    if not created:
                        print(f'Ингредиент {obj} уже есть в базе данных.')
                except Exception as error:
                    print(f'Ошибка в строке {row}: {error}')

        print(f'Файл {file_path} успешно обработан. Импорт данных завершен.') 
