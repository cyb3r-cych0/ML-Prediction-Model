from django.db import models


# Create your models here.
class DemographicInformation(models.Model):
    GENDER_CHOICES = [('0.33', 'Male'), ('0.66', 'Female'), ('1.0', 'Prefer Not Say')]
    AGE_CHOICES = [('19', '18-20'), ('23', '21-25'), ('28', '26-30'), ('33', '31-35'),
                   ('40', '36 & Above')]
    ACADEMIC_CHOICES = [('0.25', 'Freshman/First-year'), ('0.50', 'Sophomore/Second-year'), ('0.75', 'Junior/Third-year'),
                        ('1.0', 'Senior/Final-year')]
    FIELD_CHOICES = [('0.14', 'Arts/Humanities'), ('0.28', 'Business/Management'),
                     ('0.42', 'Engineering/Technology'), ('0.57', 'Sciences'),
                     ('0.71', 'Social Sciences'), ('0.85', 'Health/Medical Sciences'),
                     ('1.0', 'Other')]
    UNIVERSITY_CHOICES = [('1.0', 'Public'), ('0', 'Private')]
    UNIVERSITY_FUNDING_CHOICES = [('0.2', 'Self Sponsored'),
                                  ('0.4', 'Government Sponsored'), ('0.6', 'Scholarship'),
                                  ('0.8', 'Work Study Program'), ('1.0', 'Other')]
    MODE_OF_STUDY_CHOICES = [('0.2', 'Face to Face'), ('0.4', 'Online'), ('0.6', 'Blended'),
                             ('0.8', 'Distance Learning'), ('1.0', 'Other')]
    NET_SECURITY_KNOWLEDGE_CHOICES = [('1.0', 'Yes'), ('0', 'No')]
    SOCIAL_MEDIA_USAGE_CHOICES = [('0.2', 'Multiple times a day'), ('0.4', 'Once a day'),
                                  ('0.6', 'A few times a week'), ('0.8', 'Rarely'),
                                  ('1.0', 'Never')]
    SOCIAL_MEDIA_PLATFORMS_CHOICES = [('0.125', 'Facebook'), ('0.25', 'Instagram'), ('0.375', 'Twitter'),
                                      ('0.5', 'SnapChat'), ('0.625', 'LinkedIn'), ('0.75', 'TikTok'),
                                      ('0.875', 'YouTube'), ('1.0', 'Other')]
    AVERAGE_HOURS_ONLINE_CHOICES = [('0.33', '1HR'), ('0.66', '1-5 HRS'), ('1.0', '5 HRS')]
    LEVEL_OF_CONCERN_CHOICES = [('0.2', 'Not Concerned'), ('0.4', 'Slightly Concerned'),
                                ('0.6', 'Moderately Concerned'), ('0.8', 'Very Concerned'),
                                ('1.0', 'Extremely Concerned')]
    PRIVACY_SECURITY_BREACHES_CHOICES = [('1.0', 'Yes'), ('0', 'No')]
    SECURITY_MEASURES_CHOICES = [('0.16', 'Regular Security Updates'),
                                 ('0.33', 'Use Strong Passwords'),
                                 ('0.5', 'Enable Two Factor Auth'),
                                 ('0.66', 'Unknown Requests Cautiousness'),
                                 ('0.83', 'Avoid Share of Personal Info'),
                                 ('1.0', 'Review & Deletion of old post')]
    PRIVACY_SECURITY_EDU_CHOICES = [('1.0', 'Yes'), ('0', 'No')]
    ONLINE_SELF_PROTECTION_CHOICES = [('0.2', 'Not Confident'), ('0.4', 'Slightly Confident'),
                                      ('0.6', 'Moderately Confident'),
                                      ('0.8', 'Very Confident'),
                                      ('1.0', 'Extremely Confident')]
    PRIVACY_SETTING_AWARENESS_CHOICES = [('1', 'Yes'), ('0', 'No')]
    REVIEW_PRIVACY_SETTING_CHOICES = [('0.25', 'Regularly'), ('0.5', 'Occasionally'),
                                      ('0.75', 'Rarely'), ('1.0', 'Never')]
    PERSONAL_INFO_SHARING_CHOICES = [('0.2', 'Not Comfortable'),
                                     ('0.4', 'Slightly Comfortable'),
                                     ('0.6', 'Moderately Comfortable'),
                                     ('0.8', 'Very Comfortable'),
                                     ('1.0', 'Extremely Comfortable')]
    CYBER_BULLYING_CHOICES = [('1', 'Yes'), ('0', 'No')]
    PRIVACY_SECURITY_FEATURES_CHOICES = [('0.2', 'Very Ineffective'), ('0.4', 'Ineffective'),
                                         ('0.6', 'Neutral'), ('0.8', 'Effective'),
                                         ('1.0', 'Very Effective')]
    SENSITIVE_INFO_SHARING_CHOICES = [('1.0', 'Yes'), ('0', 'No')]
    MALICIOUS_ACTIVITY_CHOICES = [('0.25', 'Frequently'), ('0.5', 'Occasionally'), ('0.75', 'Rarely'),
                                  ('1.0', 'Never')]
    ONLINE_USER_PROTECTION_CHOICES = [('0.2', 'Strongly Agree'), ('0.4', 'Agree'), ('0.6', 'Neutral'),
                                      ('0.8', 'Disagree'), ('1.0', 'Strongly Disagree')]
    PRIVACY_POLICY_TOS_CHOICES = [('0.25', 'Very Familiar'), ('0.50', 'Somewhat Familiar'),
                                  ('0.75', 'Not Very Familiar'),
                                  ('1.0', 'Not Familiar at all')]
    SOCIAL_MEDIA_DELETION_CHOICES = [('1.0', 'Yes'), ('0', 'No')]
    SOCIAL_MEDIA_SECURITY_EDU_CHOICES = [('1.0', 'Yes'), ('0', 'No')]

    gender = models.CharField(choices=GENDER_CHOICES, max_length=15, blank=False)
    age = models.CharField(choices=AGE_CHOICES, blank=False, max_length=15)
    academic_year = models.CharField(choices=ACADEMIC_CHOICES, blank=False, max_length=25)
    field_of_study = models.CharField(choices=FIELD_CHOICES, max_length=25)
    university = models.CharField(choices=UNIVERSITY_CHOICES, max_length=30)
    university_funding = models.CharField(choices=UNIVERSITY_FUNDING_CHOICES, max_length=25)
    mode_of_study = models.CharField(choices=MODE_OF_STUDY_CHOICES, max_length=25)
    s_media_security_knowledge = models.CharField(choices=NET_SECURITY_KNOWLEDGE_CHOICES, max_length=10)
    social_media_usage = models.CharField(choices=SOCIAL_MEDIA_USAGE_CHOICES, max_length=25)
    active_social_platforms = models.CharField(choices=SOCIAL_MEDIA_PLATFORMS_CHOICES, max_length=30)
    average_hours_s_media = models.CharField(choices=AVERAGE_HOURS_ONLINE_CHOICES, max_length=15)
    s_media_security_concern = models.CharField(choices=LEVEL_OF_CONCERN_CHOICES, max_length=25)
    social_media_breaches = models.CharField(choices=PRIVACY_SECURITY_BREACHES_CHOICES, max_length=10)
    s_media_security_measure = models.CharField(choices=SECURITY_MEASURES_CHOICES, max_length=30)
    privacy_security_education = models.CharField(choices=PRIVACY_SECURITY_EDU_CHOICES, max_length=20)
    s_media_self_protection = models.CharField(choices=ONLINE_SELF_PROTECTION_CHOICES, max_length=30)
    s_media_privacy_settings_awareness = models.CharField(choices=PRIVACY_SETTING_AWARENESS_CHOICES, max_length=30)
    often_review_privacy_settings = models.CharField(choices=REVIEW_PRIVACY_SETTING_CHOICES, max_length=15)
    s_media_personal_info_sharing = models.CharField(choices=PERSONAL_INFO_SHARING_CHOICES, max_length=30)
    victim_of_cyberbullying = models.CharField(choices=CYBER_BULLYING_CHOICES, max_length=10)
    s_media_privacy_security_features = models.CharField(choices=PRIVACY_SECURITY_FEATURES_CHOICES, max_length=20)
    s_media_sensitive_info_sharing = models.CharField(choices=SENSITIVE_INFO_SHARING_CHOICES, max_length=20)
    s_media_malicious_encounters = models.CharField(choices=MALICIOUS_ACTIVITY_CHOICES, max_length=15)
    more_s_media_user_protection = models.CharField(choices=ONLINE_USER_PROTECTION_CHOICES, max_length=20)
    s_media_privacy_policy_and_TOS = models.CharField(choices=PRIVACY_POLICY_TOS_CHOICES, max_length=30)
    delete_account_due_to_privacy = models.CharField(choices=SOCIAL_MEDIA_DELETION_CHOICES, max_length=10)
    s_media_security_education = models.CharField(choices=SOCIAL_MEDIA_SECURITY_EDU_CHOICES, max_length=10)

    def __str__(self):
        return self.gender, self.academic_year

    def __int__(self):
        return self.age
