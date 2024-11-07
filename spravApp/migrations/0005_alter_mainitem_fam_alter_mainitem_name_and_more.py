# Generated by Django 5.1.1 on 2024-10-27 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spravApp', '0004_alter_mainitem_fam_alter_mainitem_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainitem',
            name='fam',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='spravApp.fam', verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='mainitem',
            name='name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='spravApp.name', verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='mainitem',
            name='otc',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='spravApp.otc', verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='mainitem',
            name='street',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='spravApp.street', verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='mainitem',
            name='tel',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True, verbose_name='Телефон'),
        ),
    ]