# Generated by Django 3.2.12 on 2022-03-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("startup", "0014_auto_20220301_1609"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="code",
            field=models.CharField(max_length=10),
        ),
    ]
