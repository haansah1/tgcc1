# Generated by Django 4.2.3 on 2024-04-30 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypd', '0018_alter_audios_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audios',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='./audio'),
        ),
    ]