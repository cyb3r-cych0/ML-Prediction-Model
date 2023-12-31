# Generated by Django 4.2 on 2023-06-30 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmtapp', '0003_alter_demographicinformation_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demographicinformation',
            name='academic_year',
            field=models.CharField(choices=[('0.25', 'Freshman/First-year'), ('0.50', 'Sophomore/Second-year'), ('0.75', 'Junior/Third-year'), ('1.0', 'Senior/Final-year')], max_length=25),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='active_social_platforms',
            field=models.CharField(choices=[('0.125', 'Facebook'), ('0.25', 'Instagram'), ('0.375', 'Twitter'), ('0.5', 'SnapChat'), ('0.625', 'LinkedIn'), ('0.75', 'TikTok'), ('0.875', 'YouTube'), ('1.0', 'Other')], max_length=30),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='age',
            field=models.CharField(choices=[('19', '18-20'), ('23', '21-25'), ('28', '26-30'), ('33', '31-35'), ('40', '36 & Above')], max_length=15),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='average_hours_s_media',
            field=models.CharField(choices=[('0.33', '1HR'), ('0.66', '1-5 HRS'), ('1.0', '5 HRS')], max_length=15),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='delete_account_due_to_privacy',
            field=models.CharField(choices=[('1.0', 'Yes'), ('0', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='field_of_study',
            field=models.CharField(choices=[('0.14', 'Arts/Humanities'), ('0.28', 'Business/Management'), ('0.42', 'Engineering/Technology'), ('0.57', 'Sciences'), ('0.71', 'Social Sciences'), ('0.85', 'Health/Medical Sciences'), ('1.0', 'Other')], max_length=25),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='gender',
            field=models.CharField(choices=[('0.33', 'Male'), ('0.66', 'Female'), ('1.0', 'Prefer Not Say')], max_length=15),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='mode_of_study',
            field=models.CharField(choices=[('0.2', 'Face to Face'), ('0.4', 'Online'), ('0.6', 'Blended'), ('0.8', 'Distance Learning'), ('1.0', 'Other')], max_length=25),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='more_s_media_user_protection',
            field=models.CharField(choices=[('0.2', 'Strongly Agree'), ('0.4', 'Agree'), ('0.6', 'Neutral'), ('0.8', 'Disagree'), ('1.0', 'Strongly Disagree')], max_length=20),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='often_review_privacy_settings',
            field=models.CharField(choices=[('0.25', 'Regularly'), ('0.5', 'Occasionally'), ('0.75', 'Rarely'), ('1.0', 'Never')], max_length=15),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='s_media_malicious_encounters',
            field=models.CharField(choices=[('0.25', 'Frequently'), ('0.5', 'Occasionally'), ('0.75', 'Rarely'), ('1.0', 'Never')], max_length=15),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='s_media_personal_info_sharing',
            field=models.CharField(choices=[('0.2', 'Not Comfortable'), ('0.4', 'Slightly Comfortable'), ('0.6', 'Moderately Comfortable'), ('0.8', 'Very Comfortable'), ('1.0', 'Extremely Comfortable')], max_length=30),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='s_media_privacy_policy_and_TOS',
            field=models.CharField(choices=[('0.25', 'Very Familiar'), ('0.50', 'Somewhat Familiar'), ('0.75', 'Not Very Familiar'), ('1.0', 'Not Familiar at all')], max_length=30),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='s_media_privacy_security_features',
            field=models.CharField(choices=[('0.2', 'Very Ineffective'), ('0.4', 'Ineffective'), ('0.6', 'Neutral'), ('0.8', 'Effective'), ('1.0', 'Very Effective')], max_length=20),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='s_media_privacy_settings_awareness',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], max_length=30),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='s_media_security_concern',
            field=models.CharField(choices=[('0.2', 'Not Concerned'), ('0.4', 'Slightly Concerned'), ('0.6', 'Moderately Concerned'), ('0.8', 'Very Concerned'), ('1.0', 'Extremely Concerned')], max_length=25),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='s_media_security_education',
            field=models.CharField(choices=[('1.0', 'Yes'), ('0', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='s_media_security_knowledge',
            field=models.CharField(choices=[('1.0', 'Yes'), ('0', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='s_media_security_measure',
            field=models.CharField(choices=[('0.16', 'Regular Security Updates'), ('0.33', 'Use Strong Passwords'), ('0.5', 'Enable Two Factor Auth'), ('0.66', 'Unknown Requests Cautiousness'), ('0.83', 'Avoid Share of Personal Info'), ('1.0', 'Review & Deletion of old post')], max_length=30),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='s_media_self_protection',
            field=models.CharField(choices=[('0.2', 'Not Confident'), ('0.4', 'Slightly Confident'), ('0.6', 'Moderately Confident'), ('0.8', 'Very Confident'), ('1.0', 'Extremely Confident')], max_length=30),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='s_media_sensitive_info_sharing',
            field=models.CharField(choices=[('1.0', 'Yes'), ('0', 'No')], max_length=20),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='social_media_breaches',
            field=models.CharField(choices=[('1.0', 'Yes'), ('0', 'No')], max_length=10),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='social_media_usage',
            field=models.CharField(choices=[('0.2', 'Multiple times a day'), ('0.4', 'Once a day'), ('0.6', 'A few times a week'), ('0.8', 'Rarely'), ('1.0', 'Never')], max_length=25),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='university',
            field=models.CharField(choices=[('1.0', 'Public'), ('0', 'Private')], max_length=30),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='university_funding',
            field=models.CharField(choices=[('0.2', 'Self Sponsored'), ('0.4', 'Government Sponsored'), ('0.6', 'Scholarship'), ('0.8', 'Work Study Program'), ('1.0', 'Other')], max_length=25),
        ),
        migrations.AlterField(
            model_name='demographicinformation',
            name='victim_of_cyberbullying',
            field=models.CharField(choices=[('1', 'Yes'), ('0', 'No')], max_length=10),
        ),
    ]
