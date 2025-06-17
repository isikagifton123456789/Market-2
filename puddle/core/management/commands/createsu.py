from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Creates a default superuser if it does not exist'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.environ.get('DJANGO_ADMIN_USERNAME', 'gifton1')
        email = os.environ.get('DJANGO_ADMIN_EMAIL', 'mwangegifton@gmail.com')
        password = os.environ.get('DJANGO_ADMIN_PASSWORD')

        if not password:
            self.stderr.write("❌ No password found in environment variable DJANGO_ADMIN_PASSWORD.")
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(f"✅ Superuser '{username}' created.")
        else:
            self.stdout.write(f"ℹ️ Superuser '{username}' already exists.")