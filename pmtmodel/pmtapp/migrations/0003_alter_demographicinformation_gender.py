# Generated by Django 4.2 on 2023-06-30 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmtapp', '0002_alter_demographicinformation_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demographicinformation',
            name='gender',
            field=models.CharField(choices=[('1', 'Male'), ('2', 'Female'), ('3', 'Prefer Not Say')], max_length=15),
        ),
    ]
