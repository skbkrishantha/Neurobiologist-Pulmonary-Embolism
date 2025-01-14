# Generated by Django 4.0.3 on 2022-04-16 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_patient_created_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medication_name', models.CharField(max_length=50)),
                ('SIG', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=50)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.patient')),
            ],
        ),
    ]
