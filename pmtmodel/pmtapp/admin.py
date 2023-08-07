from django.contrib import admin
from .models import DemographicInformation
from .models import PerceivedSeverity
from .models import PerceivedSelfEfficacy
from .models import PerceivedResponseEfficacy
from .models import PerceivedPreventionAndResponseCost
from .models import SocialNetworkSecurity


@admin.register(DemographicInformation)
class DemographicInformationAdmin(admin.ModelAdmin):
    list_display = ['gender', 'age', 'academic_year', 'predictions']
    search_fields = ['gender', 'age', 'academic_year', 'predictions']
    list_per_page = 10


@admin.register(PerceivedSeverity)
class PerceivedSeverityAdmin(admin.ModelAdmin):
    list_display = ['gender', 'age', 'academic_year', 'predictions']
    search_fields = ['gender', 'age', 'academic_year', 'predictions']
    list_per_page = 10


@admin.register(PerceivedSelfEfficacy)
class PerceivedSelfEfficacy(admin.ModelAdmin):
    list_display = ['gender', 'age', 'academic_year', 'predictions']
    search_fields = ['gender', 'age', 'academic_year', 'predictions']
    list_per_page = 10


@admin.register(PerceivedResponseEfficacy)
class PerceivedResponseEfficacy(admin.ModelAdmin):
    list_display = ['gender', 'age', 'academic_year', 'predictions']
    search_fields = ['gender', 'age', 'academic_year', 'predictions']
    list_per_page = 10


@admin.register(PerceivedPreventionAndResponseCost)
class PerceivedPreventionAndResponseCost(admin.ModelAdmin):
    list_display = ['gender', 'age', 'academic_year', 'predictions']
    search_fields = ['gender', 'age', 'academic_year', 'predictions']
    list_per_page = 10


@admin.register(SocialNetworkSecurity)
class SocialNetworkSecurity(admin.ModelAdmin):
    list_display = ['gender', 'age', 'academic_year', 'predictions']
    search_fields = ['gender', 'age', 'academic_year', 'predictions']
    list_per_page = 10
