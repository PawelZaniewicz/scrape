# Generated by Django 4.1.3 on 2022-12-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startujemy', '0002_mpk_alter_plant_mpk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
    ]
