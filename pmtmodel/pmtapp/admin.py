from django.contrib import admin
from .models import PerceivedSeverity
from .models import PerceivedVulnerability
from .models import PerceivedSelfEfficacy
from .models import PerceivedResponseEfficacy


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


@admin.register(PerceivedVulnerability)
class PerceivedVulnerability(admin.ModelAdmin):
    list_display = ['gender', 'age', 'academic_year', 'predictions']
    search_fields = ['gender', 'age', 'academic_year', 'predictions']
    list_per_page = 10
