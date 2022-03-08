from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('date_casted', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('employee', models.EmailField(max_length=254)),
                ('menu', models.UUIDField()),
            ],
            options={
                'unique_together': {('employee', 'menu')},
            },
        ),
    ]
