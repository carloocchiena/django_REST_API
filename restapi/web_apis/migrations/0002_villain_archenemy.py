# Generated by Django 4.0.2 on 2022-04-07 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_apis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Villain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(max_length=50)),
                ('villain_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Archenemy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_apis.hero')),
                ('villain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_apis.villain')),
            ],
        ),
    ]
