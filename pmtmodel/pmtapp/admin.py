from django.contrib import admin
from .models import DemographicInformation
from .models import PerceivedSeverity


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
