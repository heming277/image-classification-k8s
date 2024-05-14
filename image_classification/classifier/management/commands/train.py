from django.core.management.base import BaseCommand
from classifier.model import train_model

class Command(BaseCommand):
    help = 'Train the model'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting model training...'))
        train_model()
        self.stdout.write(self.style.SUCCESS('Model training completed.'))