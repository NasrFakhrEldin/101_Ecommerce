from django.core.management import call_command, execute_from_command_line
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Load Fixtures"

    def handle(self, *args, **options):
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "db_admin_fixture.json")
        call_command("loaddata", "db_category_fixtures.json")
