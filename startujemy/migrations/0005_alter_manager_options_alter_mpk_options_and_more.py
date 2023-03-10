# Generated by Django 4.1.3 on 2022-12-08 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startujemy', '0004_plant_manager_wmb'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': 'kierownik', 'verbose_name_plural': 'kierownicy'},
        ),
        migrations.AlterModelOptions(
            name='mpk',
            options={'verbose_name': 'mpk', 'verbose_name_plural': 'mpk'},
        ),
        migrations.AlterModelOptions(
            name='plant',
            options={'verbose_name': 'wytwórnia', 'verbose_name_plural': 'wytwórnie'},
        ),
        migrations.AddField(
            model_name='mpk',
            name='status',
            field=models.CharField(blank=True, choices=[('AKTYWNY', 'Aktywny'), ('NIEAKTYWNY', 'Nieaktywny')], max_length=10),
        ),
        migrations.AlterField(
            model_name='manager',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Imię'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Nazwisko'),
        ),
        migrations.AlterField(
            model_name='mpk',
            name='name',
            field=models.CharField(max_length=10, verbose_name='Kod MPK'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='manager_wmb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startujemy.manager', verbose_name='Kierownik WMB'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='mpk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startujemy.mpk', verbose_name='MPK'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='plant_name',
            field=models.CharField(max_length=255, verbose_name='Nazwa wytwórni'),
        ),
    ]
