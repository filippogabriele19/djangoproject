# Generated by Django 3.2.12 on 2022-02-28 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("startup", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="code",
            field=models.CharField(default="TMVIYO9D3R", max_length=10),
        ),
    ]