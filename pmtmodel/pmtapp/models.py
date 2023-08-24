from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import joblib


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
        return self.gender


# SECTION C
class PerceivedVulnerability(models.Model):
    ACADEMIC_CHOICES = [('1', 'Freshman/First-year'), ('2', 'Sophomore/Second-year'), ('3', 'Junior/Third-year'),
                        ('4', 'Senior/Final-year'), ('5', 'Other/Not a Student')]
    GENDER_CHOICES = [('1', 'Male'), ('0', 'Female'), ('2', 'Prefer Not Say')]
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

    gender = models.CharField('Gender:', choices=GENDER_CHOICES, max_length=15, blank=False)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(65)], null=True)
    academic_year = models.CharField('Level of Education:', choices=ACADEMIC_CHOICES, blank=False, max_length=25)
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
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        model = joblib.load('static/ml_efficacy_pmt.joblib')
        self.predictions = model.predict(
            [[self.security_breach_likelyness, self.vulnerable_security_breach, self.info_sharing_risk_concern,
              self.protect_info_online, self.online_potential_threats, self.update_privacy_settings,
              self.likely_2FA_authentication, self.concerned_info_breaches, self.online_info_privacy,
              self.report_suspicious_activity]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.gender


# section D
class PerceivedResponseEfficacy(models.Model):
    ACADEMIC_CHOICES = [('1', 'Freshman/First-year'), ('2', 'Sophomore/Second-year'), ('3', 'Junior/Third-year'),
                        ('4', 'Senior/Final-year'), ('5', 'Other/Not a Student')]
    GENDER_CHOICES = [('1', 'Male'), ('0', 'Female'), ('2', 'Prefer Not Say')]
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

    gender = models.CharField('Gender:', choices=GENDER_CHOICES, max_length=15, blank=False)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(65)], null=True)
    academic_year = models.CharField('Level of Education:', choices=ACADEMIC_CHOICES, blank=False, max_length=25)
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
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        model = joblib.load('static/ml_efficacy_pmt.joblib')
        self.predictions = model.predict(
            [[self.effective_security_measures, self.privacy_settings_protecting_info, self.strong_password_security,
              self.regular_security_updates, self.cautious_link_clicking, self.info_sharing_security,
              self.minimize_suspicious_individuals, self.backing_up_data, self.privacy_security_updates,
              self.sharing_info_security_reduction]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.gender


# SECTION E
class PerceivedSelfEfficacy(models.Model):
    ACADEMIC_CHOICES = [('1', 'Freshman/First-year'), ('2', 'Sophomore/Second-year'), ('3', 'Junior/Third-year'),
                        ('4', 'Senior/Final-year'), ('5', 'Other/Not a Student')]
    GENDER_CHOICES = [('1', 'Male'), ('0', 'Female'), ('2', 'Prefer Not Say')]
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

    gender = models.CharField('Gender:', choices=GENDER_CHOICES, max_length=15, blank=False)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(65)], null=True)
    academic_year = models.CharField('Level of Education:', choices=ACADEMIC_CHOICES, blank=False, max_length=25)
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
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        model = joblib.load('static/ml_efficacy_pmt.joblib')
        self.predictions = model.predict(
            [[self.effective_security_knowledge, self.security_threats_avoidance, self.privacy_setting_usage,
              self.suspicious_links_avoidance, self.suspicious_individuals_avoidance, self.antivirus_usage_knowledge,
              self.managing_social_connections, self.privacy_issues_identification, self.software_updates_security,
              self.accounts_strong_passwords]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.gender
