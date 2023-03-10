# Generated by Django 4.1.5 on 2023-02-10 05:06

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_product_call_back'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='call_back',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='product.title', unique=True),
        ),
    ]
