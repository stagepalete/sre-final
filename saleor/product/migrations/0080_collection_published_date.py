# Generated by Django 2.1.3 on 2018-12-03 20:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("product", "0079_default_tax_rate_instead_of_empty_field")]

    operations = [
        migrations.AddField(
            model_name="collection",
            name="published_date",
            field=models.DateField(blank=True, null=True),
        )
    ]
