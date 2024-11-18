# Generated by Django 4.1.13 on 2024-11-11 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shift_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
