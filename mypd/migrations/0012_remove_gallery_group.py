# Generated by Django 4.2.3 on 2024-03-04 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypd', '0011_alter_gallery_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='group',
        ),
    ]