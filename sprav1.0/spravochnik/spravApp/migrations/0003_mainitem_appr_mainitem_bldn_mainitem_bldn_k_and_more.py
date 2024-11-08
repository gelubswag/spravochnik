# Generated by Django 5.1.1 on 2024-10-27 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spravApp', '0002_mainitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainitem',
            name='appr',
            field=models.IntegerField(blank=True, null=True, verbose_name='Квартира'),
        ),
        migrations.AddField(
            model_name='mainitem',
            name='bldn',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Дом'),
        ),
        migrations.AddField(
            model_name='mainitem',
            name='bldn_k',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Корпус'),
        ),
        migrations.AddField(
            model_name='mainitem',
            name='tel',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Телефон'),
        ),
    ]
