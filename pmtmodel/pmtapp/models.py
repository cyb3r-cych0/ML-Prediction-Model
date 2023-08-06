from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import joblib


# SECTION A
class DemographicInformation(models.Model):
    GENDER_CHOICES = [('1', 'Male'), ('0', 'Female')]
    ACADEMIC_CHOICES = [('1', 'Freshman/First-year'), ('2', 'Sophomore/Second-year'), ('3', 'Junior/Third-year'),
                        ('4', 'Senior/Final-year'), ('5', 'Other/Not a Student')]
    FIELD_CHOICES = [('1', 'Arts/Humanities'), ('2', 'Business/Management'),
                     ('3', 'Engineering/Technology'), ('4', 'Sciences'),
                     ('5', 'Social Sciences'), ('6', 'Health/Medical Sciences'),
                     ('7', 'Other')]
    UNIVERSITY_CHOICES = [('1', 'Public'), ('0', 'Private')]
    UNIVERSITY_FUNDING_CHOICES = [('1', 'Self Sponsored'),
                                  ('2', 'Government Sponsored'), ('3', 'Scholarship'),
                                  ('4', 'Work Study Program'), ('5', 'Other')]
    MODE_OF_STUDY_CHOICES = [('1', 'Face to Face'), ('2', 'Online'), ('3', 'Blended'),
                             ('4', 'Distance Learning'), ('5', 'Other')]
    NET_SECURITY_KNOWLEDGE_CHOICES = [('1', 'Yes'), ('0', 'No')]
    SOCIAL_MEDIA_USAGE_CHOICES = [('1', 'Multiple times a day'), ('2', 'Once a day'),
                                  ('3', 'A few times a week'), ('4', 'Rarely'),
                                  ('5', 'Never')]
    SOCIAL_MEDIA_PLATFORMS_CHOICES = [('1', 'Facebook'), ('2', 'Instagram'), ('3', 'Twitter'),
                                      ('4', 'SnapChat'), ('5', 'LinkedIn'), ('6', 'TikTok'),
                                      ('7', 'YouTube'), ('8', 'Other')]
    AVERAGE_HOURS_ONLINE_CHOICES = [('1', '1HR'), ('2', '1-5 HRS'), ('3', '5 HRS')]
    LEVEL_OF_CONCERN_CHOICES = [('1', 'Not Concerned'), ('2', 'Slightly Concerned'),
                                ('3', 'Moderately Concerned'), ('4', 'Very Concerned'),
                                ('5', 'Extremely Concerned')]
    PRIVACY_SECURITY_BREACHES_CHOICES = [('1', 'Yes'), ('0', 'No')]
    SECURITY_MEASURES_CHOICES = [('1', 'Regular Security Updates'),
                                 ('2', 'Use Strong Passwords'),
                                 ('3', 'Enable Two Factor Auth'),
                                 ('4', 'Unknown Requests Cautiousness'),
                                 ('5', 'Avoid Share of Personal Info'),
                                 ('6', 'Review & Deletion of old post')]
    PRIVACY_SECURITY_EDU_CHOICES = [('1.0', 'Yes'), ('0', 'No')]
    ONLINE_SELF_PROTECTION_CHOICES = [('1', 'Not Confident'), ('2', 'Slightly Confident'),
                                      ('3', 'Moderately Confident'),
                                      ('4', 'Very Confident'),
                                      ('5', 'Extremely Confident')]
    PRIVACY_SETTING_AWARENESS_CHOICES = [('1', 'Yes'), ('0', 'No')]
    REVIEW_PRIVACY_SETTING_CHOICES = [('1', 'Regularly'), ('2', 'Occasionally'),
                                      ('3', 'Rarely'), ('4', 'Never')]
    PERSONAL_INFO_SHARING_CHOICES = [('1', 'Not Comfortable'),
                                     ('2', 'Slightly Comfortable'),
                                     ('3', 'Moderately Comfortable'),
                                     ('4', 'Very Comfortable'),
                                     ('5', 'Extremely Comfortable')]
    CYBER_BULLYING_CHOICES = [('1', 'Yes'), ('0', 'No')]
    PRIVACY_SECURITY_FEATURES_CHOICES = [('1', 'Very Ineffective'), ('2', 'Ineffective'),
                                         ('3', 'Neutral'), ('4', 'Effective'),
                                         ('5', 'Very Effective')]
    SENSITIVE_INFO_SHARING_CHOICES = [('1', 'Yes'), ('0', 'No')]
    MALICIOUS_ACTIVITY_CHOICES = [('1', 'Frequently'), ('2', 'Occasionally'), ('3', 'Rarely'),
                                  ('4', 'Never')]
    ONLINE_USER_PROTECTION_CHOICES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'),
                                      ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    PRIVACY_POLICY_TOS_CHOICES = [('1', 'Very Familiar'), ('2', 'Somewhat Familiar'),
                                  ('3', 'Not Very Familiar'),
                                  ('4', 'Not Familiar at all')]
    SOCIAL_MEDIA_DELETION_CHOICES = [('1', 'Yes'), ('0', 'No')]
    SOCIAL_MEDIA_SECURITY_EDU_CHOICES = [('1', 'Yes'), ('0', 'No')]

    gender = models.CharField('Gender:', choices=GENDER_CHOICES, max_length=15, blank=False)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(65)], null=True)
    academic_year = models.CharField('Academic Year:', choices=ACADEMIC_CHOICES, blank=False, max_length=25)
    field_of_study = models.CharField('Field of Study:', choices=FIELD_CHOICES, max_length=25)
    university = models.CharField('Which Kind of University Do You Attend?', choices=UNIVERSITY_CHOICES, max_length=30)
    university_funding = models.CharField('Which Mode of University Funding Do You Have?', choices=UNIVERSITY_FUNDING_CHOICES, max_length=25)
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
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    # override save to make predictions
    def save(self, *args, **kwargs):
        ml_model = joblib.load('static/ml_cybersecurity_pmt.joblib')
        self.predictions = ml_model.predict(
            [[self.gender, self.age, self.academic_year, self.field_of_study, self.university, self.university_funding,
              self.mode_of_study, self.s_media_security_knowledge, self.social_media_usage, self.active_social_platforms,
              self.average_hours_s_media, self.s_media_security_concern, self.social_media_breaches,
              self.s_media_security_measure, self.privacy_security_education, self.s_media_self_protection,
              self.s_media_privacy_settings_awareness, self.often_review_privacy_settings, self.s_media_personal_info_sharing,
              self.victim_of_cyberbullying, self.s_media_privacy_security_features, self.s_media_sensitive_info_sharing,
              self.s_media_malicious_encounters, self.more_s_media_user_protection, self.s_media_privacy_policy_and_TOS,
              self.delete_account_due_to_privacy, self.s_media_security_education]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.gender


# SECTION B
class PerceivedSeverity(models.Model):
    ACADEMIC_CHOICES = [('1', 'Freshman/First-year'), ('2', 'Sophomore/Second-year'), ('3', 'Junior/Third-year'),
                        ('4', 'Senior/Final-year'), ('5', 'Other/Not a Student')]
    GENDER_CHOICES = [('1', 'Male'), ('0', 'Female'), ('2', 'Prefer Not Say')]
    POTENTIAL_BREACH_CONSEQUENCES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    INFO_BREACH_IMPACT_CONSEQUENCES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SUBSTANTIAL_HARM_BY_BREACHES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    S_MEDIA_THREAT_CONCERN = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    NEGATIVE_IMPACTS_ON_BREACHES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    INFO_SHARING_RISKS = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SERIOUS_S_MEDIA_SECURITY = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    SUBSTANTIAL_DATA_BREACHES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    HIGH_NETWORK_SEVERITY = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]
    S_MEDIA_NEGATIVE_CONSEQUENCES = [('1', 'Strongly Agree'), ('2', 'Agree'), ('3', 'Neutral'), ('4', 'Disagree'), ('5', 'Strongly Disagree')]

    gender = models.CharField('Gender:', choices=GENDER_CHOICES, max_length=15, blank=False)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(65)], null=True)
    academic_year = models.CharField('Level of Education:', choices=ACADEMIC_CHOICES, blank=False, max_length=25)
    potential_breach_consequences = models.CharField('The potential consequences of security breaches on social networks are severe.', choices=POTENTIAL_BREACH_CONSEQUENCES, max_length=20)
    impact_of_info = models.CharField('The impact of unauthorized access to personal information on social networks is significant.', choices=INFO_BREACH_IMPACT_CONSEQUENCES, max_length=20)
    substantial_harm_by_breaches = models.CharField('The potential harm caused by privacy breaches in social network settings is substantial.', choices=SUBSTANTIAL_HARM_BY_BREACHES, max_length=20)
    s_media_threats_concern = models.CharField('The severity of threats to social network security is something I am concerned about.', choices=S_MEDIA_THREAT_CONCERN, max_length=20)
    negative_impacts_breaches = models.CharField('I believe that security breaches on social networks can lead to serious negative consequences.', choices=NEGATIVE_IMPACTS_ON_BREACHES, max_length=20)
    info_sharing_risks = models.CharField('The potential risks associated with sharing personal information on social networks are significant.', choices=INFO_SHARING_RISKS, max_length=20)
    serious_s_media_security = models.CharField('The severity of threats to social network security is something that should be taken seriously.', choices=SERIOUS_S_MEDIA_SECURITY, max_length=20)
    substantial_data_breaches = models.CharField('The potential harm caused by data breaches on social networks is substantial.', choices=SUBSTANTIAL_DATA_BREACHES, max_length=20)
    high_network_severity = models.CharField('I perceive the severity of threats to social network security as high.', choices=HIGH_NETWORK_SEVERITY, max_length=20)
    s_media_negative_consequences = models.CharField('The negative consequences of security vulnerabilities in social network settings are significant.', choices=S_MEDIA_NEGATIVE_CONSEQUENCES, max_length=20, blank=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        model = joblib.load('static/ml_efficacy_pmt.joblib')
        self.predictions = model.predict(
            [[self.potential_breach_consequences, self.impact_of_info, self.substantial_data_breaches,
                self.s_media_threats_concern, self.negative_impacts_breaches, self.info_sharing_risks,
                self.serious_s_media_security, self.substantial_data_breaches, self.high_network_severity,
                self.s_media_negative_consequences]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

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

    security_breach_likelyness = models.CharField('I believe that social network users are likely to experience security threats or breaches.', choices=SECURITY_BREACH_LIKELYNESS, max_length=20)
    vulnerable_security_breach = models.CharField('I feel personally vulnerable to security threats or breaches in social networks.', choices=VULNERABLE_SECURITY_BREACH, max_length=20)
    info_sharing_risk_concern = models.CharField('I am concerned about the potential risks associated with sharing personal information on social networks.', choices=INFO_SHARING_RISK_CONCERN, max_length=20)
    protect_info_online = models.CharField('I have confidence in my ability to protect my personal information on social networks.', choices=PROTECT_INFO_ONLINE, max_length=20)
    online_potential_threats = models.CharField('I am aware of the potential security threats and vulnerabilities present in social networks.', choices=ONLINE_POTENTIAL_THREATS, max_length=20)
    update_privacy_settings = models.CharField('I frequently review and update my privacy settings on social networks.', choices=UPDATE_PRIVACY_SETTINGS, max_length=20)
    likely_2FA_authentication = models.CharField('I am likely to use additional security measures (such as two-factor authentication) on social networks.', choices=LIKELY_2FA_AUTHENTICATION, max_length=20)
    concerned_info_breaches = models.CharField('I am concerned about the potential consequences of security breaches on my personal information and privacy.', choices=CONCERNED_INFO_BREACHES, max_length=20)
    online_info_privacy = models.CharField('I frequently engage in discussions or seek information about online privacy and security.', choices=ONLINE_INFO_PRIVACY, max_length=20)
    report_suspicious_activity = models.CharField('I am likely to report suspicious or potentially harmful activities on social networks.', choices=REPORT_SUSPICIOUS_ACTIVITY, max_length=20)

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

    effective_security_measures = models.CharField('The recommended security measures provided to protect social network accounts are effective.', choices=EFFECTIVE_SECURITY_CHOICES, max_length=20)
    privacy_settings_protecting_info = models.CharField('I believe that implementing privacy settings on social networks can effectively protect my personal information.', choices=PRIVACY_SETTINGS_PROTECTING_INFO, max_length=20)
    strong_password_security = models.CharField('I am confident that using strong and unique passwords for my social network accounts enhances their security.', choices=STRONG_PASSWORD_SECURITY, max_length=20)
    regular_security_updates = models.CharField('I trust that regularly updating my software and applications on social networks helps to mitigate security risks.', choices=REGULAR_SECURITY_UPDATES, max_length=20)
    cautious_link_clicking = models.CharField('I believe that being cautious while clicking on links and downloading files reduces the likelihood of security breaches.', choices=CAUTIOUS_LINK_CLICKING, max_length=20)
    info_sharing_security = models.CharField('I trust that being selective about the information I share on social networks helps to protect my privacy and security.', choices=INFO_SHARING_SECURITY, max_length=20)
    minimize_suspicious_individuals = models.CharField('I believe that avoiding interactions with suspicious or unknown individuals on social networks minimizes security risks.', choices=MINIMIZE_SUSPICIOUS_INDIVIDUALS, max_length=20)
    backing_up_data = models.CharField('I am confident that regularly backing up my social network data safeguards against potential data loss or security breaches.', choices=BACKING_UP_DATA, max_length=20)
    privacy_security_updates = models.CharField('I believe that being aware of and promptly updating my social network privacy policy can enhance my security and protect against unauthorized access.', choices=PRIVACY_SECURITY_UPDATES, max_length=20)
    sharing_info_security_reduction = models.CharField('I believe that being cautious about accepting friend requests and sharing personal information with strangers on social networks can reduce security risks.', choices=SHARING_INFO_SECURITY_REDUCTION, max_length=20)

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

    effective_security_knowledge = models.CharField('I believe that I possess the necessary knowledge and skills to implement effective security measures on my social network accounts.', choices=EFFECTIVE_SECURITY_KNOWLEDGE, max_length=20)
    security_threats_avoidance = models.CharField('I am confident that I can identify and avoid potential security risks and threats on social networks.', choices=SECURITY_THREATS_AVOIDANCE, max_length=20)
    privacy_setting_usage = models.CharField('I believe that I have the ability to use privacy settings effectively to control the visibility of my personal information on social networks.', choices=PRIVACY_SETTING_USAGE, max_length=20)
    suspicious_links_avoidance = models.CharField('I believe that I can recognize and avoid clicking on suspicious links or downloading malicious files on social networks.', choices=SUSPICIOUS_LINKS_AVOIDANCE, max_length=20)
    suspicious_individuals_avoidance = models.CharField('I am confident that I can recognize and avoid interacting with suspicious or unknown individuals on social networks.', choices=SUSPICIOUS_INDIVIDUALS_AVOIDANCE, max_length=20)
    antivirus_usage_knowledge = models.CharField('I believe that I have the necessary knowledge and tools to install and utilize antivirus software or security applications for my social network activities.', choices=ANTIVIRUS_USAGE_KNOWLEDGE, max_length=20)
    managing_social_connections = models.CharField('I feel capable of managing my social network connections and interactions to ensure privacy and security.', choices=MANAGING_SOCIAL_CONNECTIONS, max_length=20)
    privacy_issues_identification = models.CharField('I believe I have the necessary skills to identify and address potential privacy and security issues on social networks.', choices=PRIVACY_ISSUE_IDENTIFICATION, max_length=20)
    software_updates_security = models.CharField('I believe I have the resources and knowledge to update my software and applications regularly to enhance security.', choices=SOFTWARE_UPDATES_SECURITY, max_length=20)
    accounts_strong_passwords = models.CharField('I feel capable of using strong and unique passwords for my social network accounts.', choices=ACCOUNTS_STRONG_PASSWORDS, max_length=20)

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

    security_implementation_efforts_high = models.CharField('The effort required to implement security measures on social networks is too high.', choices=SECURITY_IMPLEMENTATION_EFFORTS_HIGH, max_length=20)
    security_financial_enhancing_high = models.CharField('The financial cost associated with enhancing security on social networks is excessive.', choices=SECURITY_FINANCIAL_ENHANCING_HIGH, max_length=20)
    security_efforts_practices_high = models.CharField('It requires a lot of effort to keep up with the latest security practices on social networks.', choices=SECURITY_EFFORTS_PRACTICES_HIGH, max_length=20)
    security_inconvenience_outweighs_benefits = models.CharField('The inconvenience caused by implementing security measures on social networks outweighs the benefits.', choices=SECURITY_INCONVENIENCE_OUTWEIGHS_BENEFITS, max_length=20)
    security_loss_functionality_undesirable = models.CharField('The potential loss of functionality or features due to enhanced security measures on social networks is undesirable.', choices=SECURITY_LOSS_FUNCTIONALITY_UNDESIRABLE, max_length=20)
    security_incidence_response_overwhelming = models.CharField('The response cost of dealing with security incidents or breaches on social networks is overwhelming.', choices=SECURITY_INCIDENCE_RESPONSE_OVERWHELMING, max_length=20)
    security_financial_cost_reasonable = models.CharField('The financial cost associated with securing my social network accounts is reasonable.', choices=SECURITY_FINANCIAL_COST_REASONABLE, max_length=20)
    security_updates_time_and_efforts_reasonable = models.CharField('The time and effort needed to regularly update software and applications for enhanced security is reasonable.', choices=SECURITY_UPDATES_TIME_AND_EFFORTS_REASONABLE, max_length=20)
    security_potential_risks_outweighs_implementations = models.CharField('The potential risks associated with not taking preventive measures on social networks outweigh the effort required to implement them.', choices=SECURITY_POTENTIAL_RISKS_OUTWEIGHS_IMPLEMENTATION, max_length=20)
    security_potential_risks_outweighs_implementation = models.CharField('The potential risks associated with not taking preventive measures on social networks outweigh the effort required to implement them.', choices=SECURITY_POTENTIAL_RISKS_OUTWEIGHS_IMPLEMENTATION, max_length=20)

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

    privacy_personal_info_maintenance = models.CharField('I am committed to maintaining the privacy of my personal information on social media platforms.', choices=PRIVACY_PERSONAL_INFO_MAINTENANCE, max_length=20)
    proactive_personal_info_access_management = models.CharField('I proactively manage my privacy settings on social media to control who can access my information.', choices=PROACTIVE_PERSONAL_INFO_ACCESS_MANAGEMENT, max_length=20)
    use_of_security_features = models.CharField('I am attentive to the security features offered by social media platforms and make use of them.', choices=USE_OF_SECURITY_FEATURES, max_length=20)
    personal_info_risk_consciousness = models.CharField('I am conscious of the potential risks associated with sharing personal information on social media.', choices=PERSONAL_INFO_RISK_CONSCIOUSNESS, max_length=20)
    secure_account_with_regular_updates = models.CharField('I intend to update my software and applications regularly to ensure the security of my social media accounts.', choices=SECURE_ACCOUNT_WITH_REGULAR_UPDATES, max_length=20)
    learn_social_network_security = models.CharField('I actively seek information and resources to enhance my knowledge of social network security.', choices=LEARN_SOCIAL_NETWORK_SECURITY, max_length=20)
    interacting_with_suspicious_accounts = models.CharField('I am cautious about interacting with unfamiliar or suspicious accounts on social media platforms.', choices=INTERACTING_WITH_SUSPICIOUS_ACCOUNTS, max_length=20)
    block_report_suspicious_accounts = models.CharField('I intend to report or block accounts that engage in inappropriate or harmful behavior on social media networks.',choices=BLOCK_REPORT_SUSPICIOUS_ACCOUNTS, max_length=20)
    educate_social_network_security = models.CharField('I have the intention to engage in discussions and educate others about the importance of social network security.', choices=EDUCATE_SOCIAL_NETWORK_SECURITY, max_length=20)
    mind_privacy_policies_before_using = models.CharField('I am mindful of the privacy policies and terms of service of social media platforms before using them.', choices=MIND_PRIVACY_POLICIES_BEFORE_USING, max_length=20)

    def __str__(self):
        return self.privacy_personal_info_maintenance
