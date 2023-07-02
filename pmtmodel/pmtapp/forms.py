from django import forms
from django.forms import ModelForm
from .models import DemographicInformation
from .models import PerceivedSeverity
from .models import PerceivedVulnerability
from .models import PerceivedResponseEfficacy
from .models import PerceivedSelfEfficacy
from .models import PerceivedPreventionAndResponseCost
from .models import IntendedUserBehaviourInSocialNetworkSecurity


class DemographicInformationForm(ModelForm):
    class Meta:
        model = DemographicInformation
        fields = "__all__"


class PerceivedSeverityForm(ModelForm):
    class Meta:
        model = PerceivedSeverity
        fields = "__all__"


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


class IntendedUserBehaviourInSocialNetworkSecurityForm(ModelForm):
    class Meta:
        model = IntendedUserBehaviourInSocialNetworkSecurity
        fields = "__all__"
