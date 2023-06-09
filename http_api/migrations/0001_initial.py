# Generated by Django 3.2.4 on 2023-05-04 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='http_api.city')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('house_number', models.CharField(max_length=10)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='http_api.city')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='http_api.street')),
            ],
        ),
    ]
