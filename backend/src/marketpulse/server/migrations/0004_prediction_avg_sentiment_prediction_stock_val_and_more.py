# Generated by Django 4.2.7 on 2023-12-21 22:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("server", "0003_merge_20231221_2222"),
    ]

    operations = [
        migrations.AddField(
            model_name="prediction",
            name="avg_sentiment",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="prediction",
            name="stock_val",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="prediction",
            name="tweet_rate",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="trainsentimentdata",
            name="sentiment",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(2),
                    django.core.validators.MinValueValidator(0),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="validsentimentdata",
            name="sentiment",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MaxValueValidator(2),
                    django.core.validators.MinValueValidator(0),
                ]
            ),
        ),
    ]