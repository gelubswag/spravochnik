# Generated by Django 5.1.1 on 2024-10-29 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spravApp', '0012_alter_mainitem_fam_alter_mainitem_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phones',
            name='val',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Телефон'),
        ),
    ]
