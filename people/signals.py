from django.core.management import call_command


def load_fixtures(sender, **kwargs):
    call_command('loaddata', 'people/fixtures/people.json')
