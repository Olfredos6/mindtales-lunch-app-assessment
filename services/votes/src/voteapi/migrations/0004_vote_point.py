# Generated by Django 4.0 on 2022-03-10 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voteapi', '0003_alter_vote_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='point',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
