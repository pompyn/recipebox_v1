# Generated by Django 2.0.2 on 2021-08-12 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0002_auto_20210811_2227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='descripton',
            new_name='description',
        ),
    ]