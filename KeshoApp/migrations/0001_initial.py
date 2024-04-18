# Generated by Django 5.0.3 on 2024-04-15 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryStay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Babe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('location', models.CharField(blank=True, max_length=10, null=True)),
                ('NameOfPersonBringingBabe', models.CharField(blank=True, max_length=200, null=True)),
                ('TimeIn', models.DateTimeField(blank=True, null=True)),
                ('TimeOut', models.DateTimeField(blank=True, null=True)),
                ('c_stay', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='KeshoApp.categorystay')),
            ],
        ),
    ]
