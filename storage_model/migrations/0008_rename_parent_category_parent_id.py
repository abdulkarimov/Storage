# Generated by Django 4.0 on 2021-12-27 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage_model', '0007_rename_category_id_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='parent',
            new_name='parent_id',
        ),
    ]