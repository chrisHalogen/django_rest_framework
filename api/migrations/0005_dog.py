# Generated by Django 3.2.4 on 2021-11-14 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211111_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
