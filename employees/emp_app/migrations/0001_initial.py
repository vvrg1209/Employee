# Generated by Django 4.2.8 on 2024-03-08 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
