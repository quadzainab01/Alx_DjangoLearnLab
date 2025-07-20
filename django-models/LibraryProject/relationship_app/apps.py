# LibraryProject/relationship_app/apps.py

from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'LibraryProject.relationship_app'  # note the full dotted path here
