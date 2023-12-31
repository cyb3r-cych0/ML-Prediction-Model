# Generated by Django 4.2 on 2023-08-05 22:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmtapp', '0020_alter_perceivedseverity_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perceivedseverity',
            name='academic_year',
            field=models.CharField(choices=[('1', 'Freshman/First-year'), ('2', 'Sophomore/Second-year'), ('3', 'Junior/Third-year'), ('4', 'Senior/Final-year'), ('5', 'Other/Not a Student')], default=1, max_length=25, verbose_name='Level of Education:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perceivedseverity',
            name='age',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(65)]),
        ),
        migrations.AddField(
            model_name='perceivedseverity',
            name='gender',
            field=models.CharField(choices=[('1', 'Male'), ('0', 'Female'), ('2', 'Prefer Not Say')], default=1, max_length=15, verbose_name='Gender:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perceivedseverity',
            name='s_media_negative_consequences',
            field=models.CharField(blank=True, choices=[('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')], max_length=20, verbose_name='The negative consequences of security vulnerabilities in social network settings are significant.'),
        ),
    ]
