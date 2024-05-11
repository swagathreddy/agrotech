# Generated by Django 4.2.7 on 2024-04-19 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agritourism', '0002_farmer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]