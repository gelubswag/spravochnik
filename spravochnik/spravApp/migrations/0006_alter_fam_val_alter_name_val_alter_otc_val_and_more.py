# Generated by Django 5.1.1 on 2024-10-28 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spravApp', '0005_alter_mainitem_fam_alter_mainitem_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fam',
            name='val',
            field=models.CharField(blank=True, max_length=30, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='name',
            name='val',
            field=models.CharField(blank=True, max_length=30, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='otc',
            name='val',
            field=models.CharField(blank=True, max_length=30, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='street',
            name='val',
            field=models.CharField(blank=True, max_length=30, verbose_name='Улица'),
        ),
    ]
