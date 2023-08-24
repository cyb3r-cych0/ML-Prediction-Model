from django import forms
from django.forms import ModelForm
from .models import PerceivedSeverity
from .models import PerceivedVulnerability
from .models import PerceivedResponseEfficacy
from .models import PerceivedSelfEfficacy


class PerceivedSeverityForm(ModelForm):
    class Meta:
        model = PerceivedSeverity
        fields = ['gender', 'age', 'academic_year', 'potential_breach_consequences', 'impact_of_info', 'substantial_harm_by_breaches', 's_media_threats_concern',
                  'negative_impacts_breaches', 'info_sharing_risks', 'serious_s_media_security',
                  'substantial_data_breaches', 'high_network_severity', 's_media_negative_consequences']


class PerceivedVulnerabilityForm(ModelForm):
    class Meta:
        model = PerceivedVulnerability
        fields = ['gender', 'age', 'academic_year', 'security_breach_likelyness', 'vulnerable_security_breach', 'info_sharing_risk_concern',
                  'protect_info_online', 'online_potential_threats', 'update_privacy_settings',
                  'likely_2FA_authentication', 'concerned_info_breaches', 'online_info_privacy', 'report_suspicious_activity']


class PerceivedResponseEfficacyForm(ModelForm):
    class Meta:
        model = PerceivedResponseEfficacy
        fields = ['gender', 'age', 'academic_year', 'effective_security_measures', 'privacy_settings_protecting_info', 'strong_password_security',
                  'regular_security_updates', 'cautious_link_clicking', 'info_sharing_security',
                  'minimize_suspicious_individuals', 'backing_up_data', 'privacy_security_updates', 'sharing_info_security_reduction']


class PerceivedSelfEfficacyForm(ModelForm):
    class Meta:
        model = PerceivedSelfEfficacy
        fields = ['gender', 'age', 'academic_year', 'effective_security_knowledge', 'security_threats_avoidance', 'privacy_setting_usage',
                  'suspicious_links_avoidance', 'suspicious_individuals_avoidance', 'antivirus_usage_knowledge',
                  'managing_social_connections', 'privacy_issues_identification', 'software_updates_security', 'accounts_strong_passwords']
