# Generated by Django 3.2.12 on 2022-03-01 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("startup", "0013_auto_20220228_1951"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lastip",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="code",
            field=models.CharField(default="1A2MG19835", max_length=10),
        ),
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="stepproduct",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]