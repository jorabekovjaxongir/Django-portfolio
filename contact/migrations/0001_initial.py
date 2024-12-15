# Generated by Django 5.1.3 on 2024-12-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=202)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=202)),
                ('message', models.TextField()),
                ('is_published', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=202)),
                ('phone', models.CharField(max_length=202)),
                ('email', models.EmailField(max_length=254)),
                ('telegram', models.CharField(max_length=150)),
                ('website', models.CharField(max_length=202)),
            ],
        ),
    ]
