# Generated by Django 4.2.3 on 2024-04-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypd', '0012_remove_gallery_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('testimony', models.CharField(max_length=5000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
