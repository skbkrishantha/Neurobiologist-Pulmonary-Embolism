# Generated by Django 4.0.3 on 2022-04-12 19:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_ctpa_probability_of_pe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='last_updated',
            field=models.DateTimeField(default=models.DateTimeField(default=django.utils.timezone.now), null=True),
        ),
    ]
