# Generated by Django 2.2 on 2022-02-28 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("startup", "0011_auto_20220228_1938"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="code",
            field=models.CharField(default="TK2QV9MI8H", max_length=10),
        ),
    ]
