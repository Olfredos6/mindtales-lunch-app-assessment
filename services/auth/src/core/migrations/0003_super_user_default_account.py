import os
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_initial'),
    ]

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth import get_user_model

        User = get_user_model()

        print("---------------> GOT GERE 1")

        # DJANGO_DB_NAME = os.environ.get('DJANGO_DB_NAME', "default")
        # DJANGO_SU_NAME = os.environ.get('DJANGO_SU_NAME')
        DJANGO_SU_EMAIL = os.environ.get('DJANGO_SU_EMAIL')
        DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SU_PASSWORD')

        superuser = User.objects.create_superuser(
            username=DJANGO_SU_EMAIL,
            email=DJANGO_SU_EMAIL,
            password=DJANGO_SU_PASSWORD
        )
        print("---------------> GOT GERE 2")

        superuser.save()
        print("---------------> GOT GERE 3")

    operations = [
        migrations.RunPython(generate_superuser),
    ]
