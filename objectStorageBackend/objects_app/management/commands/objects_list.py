from django.core.management.base import BaseCommand
from objects_app.utils import objects_list
from django.conf import settings


class Command(BaseCommand):
    help = 'Create an S3 bucket'

    def handle(self, *args, **options):
        bucket_name = 'object-storage-web-project'

        success = objects_list(bucket_name)

        if success:
            self.stdout.write(self.style.SUCCESS('List of objects showed successfully'))
        else:
            self.stdout.write(self.style.ERROR('Failed to show list of objets'))