from django.core.management import call_command
from django.core.management.base import BaseCommand
from ecommerce.promotion.setup_schedule import setup_schedule


class Command(BaseCommand):
    help = "Run the schedule_setup function"

    def handle(self, *args, **options):
        setup_schedule()
