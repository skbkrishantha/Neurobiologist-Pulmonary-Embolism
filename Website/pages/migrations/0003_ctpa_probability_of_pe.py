# Generated by Django 4.0.3 on 2022-04-11 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_patient_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='ctpa',
            name='probability_of_PE',
            field=models.DecimalField(decimal_places=7, default=0.0, max_digits=8),
        ),
    ]
