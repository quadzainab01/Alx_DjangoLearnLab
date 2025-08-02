from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

class Command(BaseCommand):
    help = 'Sets up custom permissions for the Book model'

    def handle(self, *args, **kwargs):
        Book = apps.get_model('bookshelf', 'Book')
        content_type = ContentType.objects.get_for_model(Book)

        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

        for codename, name in permissions:
            permission, created = Permission.objects.get_or_create(
                codename=codename,
                name=name,
                content_type=content_type
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created permission: {name}"))
            else:
                self.stdout.write(f"Permission already exists: {name}")
