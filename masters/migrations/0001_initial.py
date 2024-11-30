# Generated by Django 4.2.16 on 2024-09-23 06:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import masters.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ФИО')),
                ('is_works', models.BooleanField(default=True, verbose_name='Работает')),
            ],
            options={
                'verbose_name': 'Парикмахер',
                'verbose_name_plural': 'Парикмахеры',
            },
        ),
        migrations.CreateModel(
            name='MasterTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), masters.models.time_validator], verbose_name='Время, мин')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masters.master', verbose_name='Парикмахер')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Время выполнения',
                'verbose_name_plural': 'Время выполнения',
            },
        ),
        migrations.AddConstraint(
            model_name='mastertime',
            constraint=models.UniqueConstraint(fields=('service', 'master'), name='unique_constraint'),
        ),
    ]