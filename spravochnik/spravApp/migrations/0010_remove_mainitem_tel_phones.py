# Generated by Django 5.1.1 on 2024-10-29 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spravApp', '0009_mainitem_tel_delete_phones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainitem',
            name='tel',
        ),
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val', models.CharField(blank=True, max_length=12, null=True, unique=True, verbose_name='Телефон')),
                ('person', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='spravApp.mainitem', verbose_name='Контакт')),
            ],
        ),
    ]
