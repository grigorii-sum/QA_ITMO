# Generated by Django 3.1.3 on 2020-11-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_extendeduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='is_best',
            field=models.BooleanField(default=False),
        ),
    ]
