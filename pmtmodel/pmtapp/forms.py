from django import forms
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
        fields = "__all__"


class PerceivedResponseEfficacyForm(ModelForm):
    class Meta:
        model = PerceivedResponseEfficacy
        fields = "__all__"


class PerceivedSelfEfficacyForm(ModelForm):
    class Meta:
        model = PerceivedSelfEfficacy
        fields = "__all__"


class PerceivedPreventionAndResponseCostForm(ModelForm):
    class Meta:
        model = PerceivedPreventionAndResponseCost
        fields = "__all__"


class SocialNetworkSecurityForm(ModelForm):
    class Meta:
        model = SocialNetworkSecurity
        fields = "__all__"
