# Generated by Django 4.0.2 on 2022-04-07 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_apis', '0002_villain_archenemy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='villain',
            name='real_name',
        ),
    ]