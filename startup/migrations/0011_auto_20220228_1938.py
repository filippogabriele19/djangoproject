# Generated by Django 2.2 on 2022-02-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("startup", "0010_auto_20220228_1934"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="code",
            field=models.CharField(default="C78FXBGEPY", max_length=10),
        ),
    ]
