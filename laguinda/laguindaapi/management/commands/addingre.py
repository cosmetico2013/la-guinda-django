from django.core.management.base import BaseCommand, CommandError
from laguindaapi.models import Ingrediente

class Command(BaseCommand):
    help = 'Añade un nuevo ingrediente'

    def add_arguments(selft, parse):
        parse.add_argument('nombre', help="nombre del igrediente")
    
    def handle(self, *args, **options):
        name=options["nombre"]
        Ingrediente.objects.create(nombre=name)
        self.stdout.write('Ingrediente añadido')