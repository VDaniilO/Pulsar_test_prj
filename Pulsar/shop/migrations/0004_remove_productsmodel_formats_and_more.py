# Generated by Django 4.1.3 on 2022-12-13 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_imageformatsmodel_productsmodel_formats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsmodel',
            name='formats',
        ),
        migrations.DeleteModel(
            name='ImageFormatsModel',
        ),
    ]
