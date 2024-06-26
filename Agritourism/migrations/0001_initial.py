# Generated by Django 4.2.7 on 2024-04-19 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('farm_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('type_of_soil', models.CharField(max_length=100)),
                ('type_of_crop', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
