# Generated by Django 5.0.7 on 2024-08-05 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=255)),
                ('ingredients', models.CharField(max_length=255)),
                ('duration', models.IntegerField()),
                ('image', models.ImageField(blank=True, default=None, upload_to='images/')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]