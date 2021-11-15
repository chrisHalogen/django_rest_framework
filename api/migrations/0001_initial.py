# Generated by Django 3.2.4 on 2021-11-11 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, error_messages={'null': 'This Field Cannot be null'}, max_length=255, null=True, unique=True)),
                ('description', models.TextField()),
                ('phone_number', models.PositiveIntegerField()),
                ('is_live', models.BooleanField()),
                ('amount', models.FloatField()),
            ],
        ),
    ]