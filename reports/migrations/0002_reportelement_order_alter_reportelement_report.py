# Generated by Django 5.1 on 2024-08-16 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="reportelement",
            name="order",
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="reportelement",
            name="report",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="elements",
                to="reports.report",
            ),
        ),
    ]
