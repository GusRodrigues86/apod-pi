# Generated by Django 5.1.4 on 2024-12-06 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('date', models.TextField()),
                ('explanation', models.TextField()),
                ('rights', models.TextField()),
                ('url', models.TextField()),
            ],
        ),
    ]