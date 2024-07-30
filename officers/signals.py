from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.core.management import call_command
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from violations.models import Violation
from .models import Officer


@receiver(post_migrate)
def load_fixtures(sender, **kwargs):
    if sender.name == 'officers':
        call_command('loaddata', 'officers/fixtures/users.json')
        call_command('loaddata', 'officers/fixtures/officers.json')


@receiver(post_migrate)
def assign_permissions(sender, **kwargs):
    if sender.name == 'violations':
        content_type = ContentType.objects.get_for_model(Violation)
        view_permission = Permission.objects.get(content_type=content_type, codename='view_violation')
        change_permission = Permission.objects.get(content_type=content_type, codename='change_violation')

        officers = Officer.objects.all()
        for officer in officers:
            user = officer.user
            user.user_permissions.add(view_permission, change_permission)
            user.save()
