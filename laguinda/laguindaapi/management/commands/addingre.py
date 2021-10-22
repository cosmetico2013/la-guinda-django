from django.core.management.base import BaseCommand, CommandError
from laguindaapi.models import Ingrediente

class command(BaseCommand):
    help = 'Añade un nuevo ingrediente'

    def add_arguments(selft, parse):
        parse.add_argument('nom', help="nombre del igrediente")
    
    def handle(self, *args, **options):
        name=options["nom"]
        Ingrediente.objects.create(nom=name)
        self.stdout.write('Ingrediente añadido')