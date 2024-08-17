from django.core.management.base import BaseCommand
from objects_app.utils import upload_file


class Command(BaseCommand):
    help = 'Create an S3 bucket'

    def handle(self, *args, **options):
        bucket_name = 'object-storage-web-project'

        success = upload_file(bucket_name)

        if success:
            self.stdout.write(self.style.SUCCESS('File uploaded successfully'))
        else:
            self.stdout.write(self.style.ERROR('Failed to upload file'))