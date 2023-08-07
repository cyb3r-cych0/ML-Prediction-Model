from django.forms import ModelForm
from .models import DemographicInformation
from .models import PerceivedSeverity
from .models import PerceivedVulnerability
from .models import PerceivedResponseEfficacy
from .models import PerceivedSelfEfficacy
from .models import PerceivedPreventionAndResponseCost
from .models import SocialNetworkSecurity


class DemographicInformationForm(ModelForm):
    class Meta:
        model = DemographicInformation
        fields = ['gender', 'age', 'academic_year', 'field_of_study', 'university', 'university_funding', 'mode_of_study',
                  's_media_security_knowledge', 'social_media_usage', 'active_social_platforms', 'average_hours_s_media',
                  's_media_security_concern', 'social_media_breaches', 's_media_security_measure', 'privacy_security_education',
                  's_media_self_protection', 's_media_privacy_settings_awareness', 'often_review_privacy_settings',
                  's_media_personal_info_sharing', 'victim_of_cyberbullying', 's_media_privacy_security_features',
                  's_media_sensitive_info_sharing', 's_media_malicious_encounters', 'more_s_media_user_protection',
                  's_media_privacy_policy_and_TOS', 'delete_account_due_to_privacy', 's_media_security_education']


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


class PerceivedPreventionAndResponseCostForm(ModelForm):
    class Meta:
        model = PerceivedPreventionAndResponseCost
        fields = ['gender', 'age', 'academic_year', 'security_implementation_efforts_high', 'security_financial_enhancing_high', 'security_efforts_practices_high',
                  'security_inconvenience_outweighs_benefits', 'security_loss_functionality_undesirable', 'security_incidence_response_overwhelming',
                  'security_financial_cost_reasonable', 'security_updates_time_and_efforts_reasonable', 'security_potential_risks_outweighs_implementations', 'security_potential_risks_outweighs_implementation']


class SocialNetworkSecurityForm(ModelForm):
    class Meta:
        model = SocialNetworkSecurity
        fields = ['gender', 'age', 'academic_year', 'privacy_personal_info_maintenance', 'proactive_personal_info_access_management', 'use_of_security_features',
                  'personal_info_risk_consciousness', 'secure_account_with_regular_updates', 'learn_social_network_security',
                  'interacting_with_suspicious_accounts', 'block_report_suspicious_accounts', 'educate_social_network_security', 'mind_privacy_policies_before_using']
