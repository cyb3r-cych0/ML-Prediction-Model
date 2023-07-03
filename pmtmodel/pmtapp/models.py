from django.db import models


# SECTION A
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

    gender = models.CharField('Gender:', choices=GENDER_CHOICES, max_length=15, blank=False)
    age = models.CharField('Age:', choices=AGE_CHOICES, blank=False, max_length=15)
    academic_year = models.CharField('Academic Year:', choices=ACADEMIC_CHOICES, blank=False, max_length=25)
    field_of_study = models.CharField('Field of Study:', choices=FIELD_CHOICES, max_length=25)
    university = models.CharField('Which Kind of University Do You Attend?', choices=UNIVERSITY_CHOICES, max_length=30)
    university_funding = models.CharField('Which Model of University Funding Do You Have?', choices=UNIVERSITY_FUNDING_CHOICES, max_length=25)
    mode_of_study = models.CharField('What Mode of Study Are You Taking Your Studies?', choices=MODE_OF_STUDY_CHOICES, max_length=25)
    s_media_security_knowledge = models.CharField('Do You Have Any Prior Knowledge or Training In Social Network Security?', choices=NET_SECURITY_KNOWLEDGE_CHOICES, max_length=10)
    social_media_usage = models.CharField('How Frequently Do You Use Social Media Platforms?', choices=SOCIAL_MEDIA_USAGE_CHOICES, max_length=25)
    active_social_platforms = models.CharField('Which Social Media Platforms Do You Actively Use?', choices=SOCIAL_MEDIA_PLATFORMS_CHOICES, max_length=30)
    average_hours_s_media = models.CharField('Hour Many Hours Do You Spend Per Day On Social Media Platforms?', choices=AVERAGE_HOURS_ONLINE_CHOICES, max_length=15)
    s_media_security_concern = models.CharField('How Concerned Are You About The Security Of Your Personal Info On Social Media Platforms?', choices=LEVEL_OF_CONCERN_CHOICES, max_length=25)
    social_media_breaches = models.CharField('Have You Experienced Any Security Incidents Or Privacy Breaches On Social Media Platforms?', choices=PRIVACY_SECURITY_BREACHES_CHOICES, max_length=10)
    s_media_security_measure = models.CharField('What Measures Do You Currently Take To Enhance Your Social Network Security?', choices=SECURITY_MEASURES_CHOICES, max_length=30)
    privacy_security_education = models.CharField('Have You Received Any Privacy Or Security Education Or Training In the Past?', choices=PRIVACY_SECURITY_EDU_CHOICES, max_length=20)
    s_media_self_protection = models.CharField('How Confident Are You In Your Ability To Protect Your Privacy And Security On Social Media Platforms?', choices=ONLINE_SELF_PROTECTION_CHOICES, max_length=30)
    s_media_privacy_settings_awareness = models.CharField('Are You Aware Of The Privacy Settings Available On Social Media Platforms?', choices=PRIVACY_SETTING_AWARENESS_CHOICES, max_length=30)
    often_review_privacy_settings = models.CharField('How Often Do You Review & Adjust Your Privacy Settings On Social Media Platforms?', choices=REVIEW_PRIVACY_SETTING_CHOICES, max_length=15)
    s_media_personal_info_sharing = models.CharField('How Comfortable Are You With Sharing Personal Information On Social Media Platforms?', choices=PERSONAL_INFO_SHARING_CHOICES, max_length=30)
    victim_of_cyberbullying = models.CharField('Have You Ever Been A Victim Of Online Harassment Or Cyberbullying On Social Media Platforms?', choices=CYBER_BULLYING_CHOICES, max_length=10)
    s_media_privacy_security_features = models.CharField('How Would You Rate The Effectiveness Of The Privacy & Security Features Provided By Social Media Platforms?', choices=PRIVACY_SECURITY_FEATURES_CHOICES, max_length=20)
    s_media_sensitive_info_sharing = models.CharField('Have You Ever Shared Sensitive Information(e.g. Personal Identification, Financial Details) Through Social Media Platforms?', choices=SENSITIVE_INFO_SHARING_CHOICES, max_length=20)
    s_media_malicious_encounters = models.CharField('How Often Do you Encounter Suspicious Or Malicious Activities On Social Media Platforms(e.g. Fake Profiles, Phishing Attempts)?', choices=MALICIOUS_ACTIVITY_CHOICES, max_length=15)
    more_s_media_user_protection = models.CharField('Do You Believe Social Media Platforms Should Do More To Protect Users Privacy & Security?', choices=ONLINE_USER_PROTECTION_CHOICES, max_length=20)
    s_media_privacy_policy_and_TOS = models.CharField('How Familiar Are You With The Privacy Policies & Terms Of Service Of The Social Media Platforms?', choices=PRIVACY_POLICY_TOS_CHOICES, max_length=30)
    delete_account_due_to_privacy = models.CharField('Have You Ever Changed Or Deleted A Social Media Account Due To Privacy Or Security Concerns?', choices=SOCIAL_MEDIA_DELETION_CHOICES, max_length=10)
    s_media_security_education = models.CharField('Would You Be Willing To Participate In Educational Programs Or WorkShops Focused On Social Network Security?', choices=SOCIAL_MEDIA_SECURITY_EDU_CHOICES, max_length=10)

    def __str__(self):
        return self.gender, self.academic_year


# SECTION B
class PerceivedSeverity(models.Model):
    POTENTIAL_BREACH_CONSEQUENCES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    INFO_BREACH_IMPACT_CONSEQUENCES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SUBSTANTIAL_HARM_BY_BREACHES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    S_MEDIA_THREAT_CONCERN = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    NEGATIVE_IMPACTS_ON_BREACHES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    INFO_SHARING_RISKS = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SERIOUS_S_MEDIA_SECURITY = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SUBSTANTIAL_DATA_BREACHES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    HIGH_NETWORK_SEVERITY =[('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    S_MEDIA_NEGATIVE_CONSEQUENCES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]

    potential_breach_consequences = models.CharField(choices=POTENTIAL_BREACH_CONSEQUENCES, max_length=20)
    impact_of_info = models.CharField(choices=INFO_BREACH_IMPACT_CONSEQUENCES, max_length=20)
    substantial_harm_by_breaches = models.CharField(choices=SUBSTANTIAL_HARM_BY_BREACHES, max_length=20)
    s_media_threats_concern = models.CharField(choices=S_MEDIA_THREAT_CONCERN, max_length=20)
    negative_impacts_breaches = models.CharField(choices=NEGATIVE_IMPACTS_ON_BREACHES, max_length=20)
    info_sharing_risks = models.CharField(choices=INFO_SHARING_RISKS, max_length=20)
    serious_s_media_security = models.CharField(choices=SERIOUS_S_MEDIA_SECURITY, max_length=20)
    substantial_data_breaches = models.CharField(choices=SUBSTANTIAL_DATA_BREACHES, max_length=20)
    high_network_severity = models.CharField(choices=HIGH_NETWORK_SEVERITY, max_length=20)
    s_media_negative_consequences = models.CharField(choices=S_MEDIA_NEGATIVE_CONSEQUENCES, max_length=20)

    def __str__(self):
        return self.potential_breach_consequences


# SECTION C
class PerceivedVulnerability(models.Model):
    SECURITY_BREACH_LIKELYNESS = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    VULNERABLE_SECURITY_BREACH = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    INFO_SHARING_RISK_CONCERN = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    PROTECT_INFO_ONLINE = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    ONLINE_POTENTIAL_THREATS = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    UPDATE_PRIVACY_SETTINGS = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    LIKELY_2FA_AUTHENTICATION = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    CONCERNED_INFO_BREACHES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    ONLINE_INFO_PRIVACY = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    REPORT_SUSPICIOUS_ACTIVITY = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]

    security_breach_likelyness = models.CharField(choices=SECURITY_BREACH_LIKELYNESS, max_length=20)
    vulnerable_security_breach = models.CharField(choices=VULNERABLE_SECURITY_BREACH, max_length=20)
    info_sharing_risk_concern = models.CharField(choices=INFO_SHARING_RISK_CONCERN, max_length=20)
    protect_info_online = models.CharField(choices=PROTECT_INFO_ONLINE, max_length=20)
    online_potential_threats = models.CharField(choices=ONLINE_POTENTIAL_THREATS, max_length=20)
    update_privacy_settings = models.CharField(choices=UPDATE_PRIVACY_SETTINGS, max_length=20)
    likely_2FA_authentication = models.CharField(choices=LIKELY_2FA_AUTHENTICATION, max_length=20)
    concerned_info_breaches = models.CharField(choices=CONCERNED_INFO_BREACHES, max_length=20)
    online_info_privacy = models.CharField(choices=ONLINE_INFO_PRIVACY, max_length=20)
    report_suspicious_activity = models.CharField(choices=REPORT_SUSPICIOUS_ACTIVITY, max_length=20)

    def __str__(self):
        return self.security_breach_likelyness


# section D
class PerceivedResponseEfficacy(models.Model):
    EFFECTIVE_SECURITY_CHOICES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    PRIVACY_SETTINGS_PROTECTING_INFO = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    STRONG_PASSWORD_SECURITY = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    REGULAR_SECURITY_UPDATES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    CAUTIOUS_LINK_CLICKING = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    INFO_SHARING_SECURITY = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    MINIMIZE_SUSPICIOUS_INDIVIDUALS = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    BACKING_UP_DATA = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    PRIVACY_SECURITY_UPDATES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SHARING_INFO_SECURITY_REDUCTION = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]

    effective_security_measures = models.CharField(choices=EFFECTIVE_SECURITY_CHOICES, max_length=20)
    privacy_settings_protecting_info = models.CharField(choices=PRIVACY_SETTINGS_PROTECTING_INFO, max_length=20)
    strong_password_security = models.CharField(choices=STRONG_PASSWORD_SECURITY, max_length=20)
    regular_security_updates = models.CharField(choices=REGULAR_SECURITY_UPDATES, max_length=20)
    cautious_link_clicking = models.CharField(choices=CAUTIOUS_LINK_CLICKING, max_length=20)
    info_sharing_security = models.CharField(choices=INFO_SHARING_SECURITY, max_length=20)
    minimize_suspicious_individuals = models.CharField(choices=MINIMIZE_SUSPICIOUS_INDIVIDUALS, max_length=20)
    backing_up_data = models.CharField(choices=BACKING_UP_DATA, max_length=20)
    privacy_security_updates = models.CharField(choices=PRIVACY_SECURITY_UPDATES, max_length=20)
    sharing_info_security_reduction = models.CharField(choices=SHARING_INFO_SECURITY_REDUCTION, max_length=20)

    def __str__(self):
        return self.effective_security_measures


# SECTION E
class PerceivedSelfEfficacy(models.Model):
    EFFECTIVE_SECURITY_KNOWLEDGE = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SECURITY_THREATS_AVOIDANCE = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    PRIVACY_SETTING_USAGE = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SUSPICIOUS_LINKS_AVOIDANCE = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SUSPICIOUS_INDIVIDUALS_AVOIDANCE = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    ANTIVIRUS_USAGE_KNOWLEDGE = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    MANAGING_SOCIAL_CONNECTIONS = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    PRIVACY_ISSUE_IDENTIFICATION = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SOFTWARE_UPDATES_SECURITY = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    ACCOUNTS_STRONG_PASSWORDS = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]

    effective_security_knowledge = models.CharField(choices=EFFECTIVE_SECURITY_KNOWLEDGE, max_length=20)
    security_threats_avoidance = models.CharField(choices=SECURITY_THREATS_AVOIDANCE, max_length=20)
    privacy_setting_usage = models.CharField(choices=PRIVACY_SETTING_USAGE, max_length=20)
    suspicious_links_avoidance = models.CharField(choices=SUSPICIOUS_LINKS_AVOIDANCE, max_length=20)
    suspicious_individuals_avoidance = models.CharField(choices=SUSPICIOUS_INDIVIDUALS_AVOIDANCE, max_length=20)
    antivirus_usage_knowledge = models.CharField(choices=ANTIVIRUS_USAGE_KNOWLEDGE, max_length=20)
    managing_social_connections = models.CharField(choices=MANAGING_SOCIAL_CONNECTIONS, max_length=20)
    privacy_issues_identification = models.CharField(choices=PRIVACY_ISSUE_IDENTIFICATION, max_length=20)
    software_updates_security = models.CharField(choices=SOFTWARE_UPDATES_SECURITY, max_length=20)
    accounts_strong_passwords = models.CharField(choices=ACCOUNTS_STRONG_PASSWORDS, max_length=20)

    def __str__(self):
        return self.effective_security_knowledge


# SECTION F
class PerceivedPreventionAndResponseCost(models.Model):
    SECURITY_IMPLEMENTATION_EFFORTS_HIGH = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SECURITY_FINANCIAL_ENHANCING_HIGH = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SECURITY_EFFORTS_PRACTICES_HIGH = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SECURITY_INCONVENIENCE_OUTWEIGHS_BENEFITS = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SECURITY_LOSS_FUNCTIONALITY_UNDESIRABLE = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SECURITY_INCIDENCE_RESPONSE_OVERWHELMING = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SECURITY_FINANCIAL_COST_REASONABLE = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SECURITY_UPDATES_TIME_AND_EFFORTS_REASONABLE = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SECURITY_POTENTIAL_RISKS_OUTWEIGHS_IMPLEMENTATION = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]

    security_implementation_efforts_high = models.CharField(choices=SECURITY_IMPLEMENTATION_EFFORTS_HIGH, max_length=20)
    security_financial_enhancing_high = models.CharField(choices=SECURITY_FINANCIAL_ENHANCING_HIGH, max_length=20)
    security_efforts_practices_high = models.CharField(choices=SECURITY_EFFORTS_PRACTICES_HIGH, max_length=20)
    security_inconvenience_outweighs_benefits = models.CharField(choices=SECURITY_INCONVENIENCE_OUTWEIGHS_BENEFITS, max_length=20)
    security_loss_functionality_undesirable = models.CharField(choices=SECURITY_LOSS_FUNCTIONALITY_UNDESIRABLE, max_length=20)
    security_incidence_response_overwhelming = models.CharField(choices=SECURITY_INCIDENCE_RESPONSE_OVERWHELMING, max_length=20)
    security_financial_cost_reasonable = models.CharField(choices=SECURITY_FINANCIAL_COST_REASONABLE, max_length=20)
    security_updates_time_and_efforts_reasonable = models.CharField(choices=SECURITY_UPDATES_TIME_AND_EFFORTS_REASONABLE, max_length=20)
    security_potential_risks_outweighs_implementations = models.CharField(choices=SECURITY_POTENTIAL_RISKS_OUTWEIGHS_IMPLEMENTATION, max_length=20)

    def __str__(self):
        return self.security_implementation_efforts_high


# SECTION G
class SocialNetworkSecurity(models.Model):
    PRIVACY_PERSONAL_INFO_MAINTENANCE = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    PROACTIVE_PERSONAL_INFO_ACCESS_MANAGEMENT = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    USE_OF_SECURITY_FEATURES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    PERSONAL_INFO_RISK_CONSCIOUSNESS = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SECURE_ACCOUNT_WITH_REGULAR_UPDATES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    LEARN_SOCIAL_NETWORK_SECURITY = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    INTERACTING_WITH_SUSPICIOUS_ACCOUNTS = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    BLOCK_REPORT_SUSPICIOUS_ACCOUNTS = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    EDUCATE_SOCIAL_NETWORK_SECURITY = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    MIND_PRIVACY_POLICIES_BEFORE_USING = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]

    privacy_personal_info_maintenance = models.CharField(choices=PRIVACY_PERSONAL_INFO_MAINTENANCE, max_length=20)
    proactive_personal_info_access_management = models.CharField(choices=PROACTIVE_PERSONAL_INFO_ACCESS_MANAGEMENT, max_length=20)
    use_of_security_features = models.CharField(choices=USE_OF_SECURITY_FEATURES, max_length=20)
    personal_info_risk_consciousness = models.CharField(choices=PERSONAL_INFO_RISK_CONSCIOUSNESS, max_length=20)
    secure_account_with_regular_updates = models.CharField(choices=SECURE_ACCOUNT_WITH_REGULAR_UPDATES, max_length=20)
    learn_social_network_security = models.CharField(choices=LEARN_SOCIAL_NETWORK_SECURITY, max_length=20)
    interacting_with_suspicious_accounts = models.CharField(choices=INTERACTING_WITH_SUSPICIOUS_ACCOUNTS, max_length=20)
    block_report_suspicious_accounts = models.CharField(choices=BLOCK_REPORT_SUSPICIOUS_ACCOUNTS, max_length=20)
    educate_social_network_security = models.CharField(choices=EDUCATE_SOCIAL_NETWORK_SECURITY, max_length=20)
    mind_privacy_policies_before_using = models.CharField(choices=MIND_PRIVACY_POLICIES_BEFORE_USING, max_length=20)

    def __str__(self):
        return self.privacy_personal_info_maintenance
