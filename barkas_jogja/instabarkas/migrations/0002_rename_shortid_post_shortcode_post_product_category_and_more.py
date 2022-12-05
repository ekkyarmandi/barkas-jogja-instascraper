# Generated by Django 4.1.3 on 2022-12-05 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instabarkas", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="shortid",
            new_name="shortcode",
        ),
        migrations.AddField(
            model_name="post",
            name="product_category",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="product_label",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="is_ads",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="is_single_product",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="is_sold",
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="price",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="product_name",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="seller_username",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
