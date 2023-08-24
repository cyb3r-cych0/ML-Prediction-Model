from django.shortcuts import render, redirect
from .models import PerceivedSeverity
from .models import PerceivedVulnerability
from .models import PerceivedResponseEfficacy
from .models import PerceivedSelfEfficacy
from .forms import PerceivedSeverityForm
from .forms import PerceivedVulnerabilityForm
from .forms import PerceivedResponseEfficacyForm
from .forms import PerceivedSelfEfficacyForm
from django.db.models import Count
import datetime
from collections import Counter


def home(request):
    ps_count_threat = PerceivedSeverity.objects.filter(predictions="['THREAT']").count()
    ps_count_coping = PerceivedSeverity.objects.filter(predictions="['COPING']").count()

    # Perceived Vulnerability
    pv_count_threat = PerceivedVulnerability.objects.filter(predictions="['THREAT']").count()
    pv_count_coping = PerceivedVulnerability.objects.filter(predictions="['COPING']").count()

    # Perceived Self Efficacy
    pse_count_threat = PerceivedSelfEfficacy.objects.filter(predictions="['THREAT']").count()
    pse_count_coping = PerceivedSelfEfficacy.objects.filter(predictions="['COPING']").count()

    # Perceived Response Efficacy
    pre_count_threat = PerceivedResponseEfficacy.objects.filter(predictions="['THREAT']").count()
    pre_count_coping = PerceivedResponseEfficacy.objects.filter(predictions="['COPING']").count()

    context = {
        'ps_count_threat': ps_count_threat,
        'ps_count_coping': ps_count_coping,
        'pv_count_threat': pv_count_threat,
        'pv_count_coping': pv_count_coping,
        'pse_count_threat': pse_count_threat,
        'pse_count_coping': pse_count_coping,
        'pre_count_threat': pre_count_threat,
        'pre_count_coping': pre_count_coping,
    }
    return render(request, 'home.html', context)


def datasets(request):
    now = datetime.datetime.now()

    ps_count_freshman = PerceivedSeverity.objects.filter(academic_year='1').count()
    ps_count_sophomore = PerceivedSeverity.objects.filter(academic_year='2').count()
    ps_count_junior = PerceivedSeverity.objects.filter(academic_year='3').count()
    ps_count_senior = PerceivedSeverity.objects.filter(academic_year='4').count()
    ps_count_other = PerceivedSeverity.objects.filter(academic_year='5').count()

    ps_count_male = PerceivedSeverity.objects.filter(gender='1').count()
    ps_count_female = PerceivedSeverity.objects.filter(gender='0').count()
    ps_count_anon = PerceivedSeverity.objects.filter(gender='2').count()

    pv_count_freshman = PerceivedVulnerability.objects.filter(academic_year='1').count()
    pv_count_sophomore = PerceivedVulnerability.objects.filter(academic_year='2').count()
    pv_count_junior = PerceivedVulnerability.objects.filter(academic_year='3').count()
    pv_count_senior = PerceivedVulnerability.objects.filter(academic_year='4').count()
    pv_count_other = PerceivedVulnerability.objects.filter(academic_year='5').count()

    pv_count_male = PerceivedVulnerability.objects.filter(gender='1').count()
    pv_count_female = PerceivedVulnerability.objects.filter(gender='0').count()
    pv_count_anon = PerceivedVulnerability.objects.filter(gender='2').count()

    pse_count_freshman = PerceivedSelfEfficacy.objects.filter(academic_year='1').count()
    pse_count_sophomore = PerceivedSelfEfficacy.objects.filter(academic_year='2').count()
    pse_count_junior = PerceivedSelfEfficacy.objects.filter(academic_year='3').count()
    pse_count_senior = PerceivedSelfEfficacy.objects.filter(academic_year='4').count()
    pse_count_other = PerceivedSelfEfficacy.objects.filter(academic_year='5').count()

    pse_count_male = PerceivedSelfEfficacy.objects.filter(gender='1').count()
    pse_count_female = PerceivedSelfEfficacy.objects.filter(gender='0').count()
    pse_count_anon = PerceivedSelfEfficacy.objects.filter(gender='2').count()

    pre_count_freshman = PerceivedResponseEfficacy.objects.filter(academic_year='1').count()
    pre_count_sophomore = PerceivedResponseEfficacy.objects.filter(academic_year='2').count()
    pre_count_junior = PerceivedResponseEfficacy.objects.filter(academic_year='3').count()
    pre_count_senior = PerceivedResponseEfficacy.objects.filter(academic_year='4').count()
    pre_count_other = PerceivedResponseEfficacy.objects.filter(academic_year='5').count()

    pre_count_male = PerceivedResponseEfficacy.objects.filter(gender='1').count()
    pre_count_female = PerceivedResponseEfficacy.objects.filter(gender='0').count()
    pre_count_anon = PerceivedResponseEfficacy.objects.filter(gender='2').count()

    total_count_freshman = ps_count_freshman + pv_count_freshman + pse_count_freshman + pre_count_freshman
    total_count_sophomore = ps_count_sophomore + pv_count_sophomore + pse_count_sophomore + pre_count_sophomore
    total_count_junior = ps_count_junior + pv_count_junior + pse_count_junior + pre_count_junior
    total_count_senior = ps_count_senior + pv_count_senior + pse_count_senior + pre_count_senior
    total_count_other = ps_count_other + pv_count_other + pse_count_other + pre_count_other

    all_male = ps_count_male + pv_count_male + pse_count_male + pre_count_male
    all_female = ps_count_female + pv_count_female + pse_count_female + pre_count_female
    all_anon = ps_count_anon + pv_count_anon + pse_count_anon + pre_count_anon

    # Perceived Severity
    ps = PerceivedSeverity.objects.all()
    ps_number = ps.count()
    ps_age = sum(ps.values_list('age', flat=True))
    try:
        ps_avg_age = int(ps_age / ps_number)
    except ZeroDivisionError:
        ps_avg_age = 0

    ps_count_threat = PerceivedSeverity.objects.filter(predictions="['THREAT']").count()
    ps_count_coping = PerceivedSeverity.objects.filter(predictions="['COPING']").count()
    if ps_count_threat > ps_count_coping:
        ps_pred_value = 'THREAT APPRAISED'
    elif ps_count_coping > ps_count_threat:
        ps_pred_value = 'COPING APPRAISED'
    else:
        ps_pred_value = 'UNCATEGORIZED YET'

    # Perceived Vulnerability
    pv = PerceivedVulnerability.objects.all()
    pv_number = pv.count()
    pv_age = sum(pv.values_list('age', flat=True))
    try:
        pv_avg_age = int(pv_age / pv_number)
    except ZeroDivisionError:
        pv_avg_age = 0

    pv_count_threat = PerceivedVulnerability.objects.filter(predictions="['THREAT']").count()
    pv_count_coping = PerceivedVulnerability.objects.filter(predictions="['COPING']").count()
    if pv_count_threat > pv_count_coping:
        pv_pred_value = 'THREAT APPRAISED'
    elif pv_count_coping > pv_count_threat:
        pv_pred_value = 'COPING APPRAISED'
    else:
        pv_pred_value = 'UNCATEGORIZED YET'

    # Perceived Self Efficacy
    pse = PerceivedSelfEfficacy.objects.all()
    pse_number = pse.count()
    pse_age = sum(pse.values_list('age', flat=True))
    try:
        pse_avg_age = int(pse_age / pse_number)
    except ZeroDivisionError:
        pse_avg_age = 0

    pse_count_threat = PerceivedSelfEfficacy.objects.filter(predictions="['THREAT']").count()
    pse_count_coping = PerceivedSelfEfficacy.objects.filter(predictions="['COPING']").count()
    if pse_count_threat > pse_count_coping:
        pse_pred_value = 'THREAT APPRAISED'
    elif pse_count_coping > pse_count_threat:
        pse_pred_value = 'COPING APPRAISED'
    else:
        pse_pred_value = 'UNCATEGORIZED YET'

    # Perceived Response Efficacy
    pre = PerceivedResponseEfficacy.objects.all()
    pre_number = pre.count()
    pre_age = sum(pre.values_list('age', flat=True))
    try:
        pre_avg_age = int(pre_age / pre_number)
    except ZeroDivisionError:
        pre_avg_age = 0

    pre_count_threat = PerceivedResponseEfficacy.objects.filter(predictions="['THREAT']").count()
    pre_count_coping = PerceivedResponseEfficacy.objects.filter(predictions="['COPING']").count()
    if pre_count_threat > pre_count_coping:
        pre_pred_value = 'THREAT APPRAISED'
    elif pre_count_coping > pre_count_threat:
        pre_pred_value = 'COPING APPRAISED'
    else:
        pre_pred_value = 'UNCATEGORIZED YET'

    # sum
    total_number = ps_number + pv_number + pse_number + pre_number
    total_avg_age = ps_avg_age + pv_avg_age + pse_avg_age + pre_avg_age
    avg_avg_age = int(total_avg_age / 4)

    total_threat = ps_count_threat + pv_count_threat + pse_count_threat + pre_count_threat
    total_coping = ps_count_coping + pv_count_coping + pse_count_coping + pre_count_coping

    if total_threat > total_coping:
        final_pred = 'THREAT APPRAISAL'
    elif total_coping > total_threat:
        final_pred = 'COPING APPRAISAL'
    else:
        final_pred = 'UNCATEGORIZED YET'

    context = {
        'all_male': all_male,
        'all_female': all_female,
        'all_anon': all_anon,
        'ps_count_freshman': ps_count_freshman,
        'ps_count_sophomore': ps_count_sophomore,
        'ps_count_junior': ps_count_junior,
        'ps_count_senior': ps_count_senior,
        'ps_count_other': ps_count_other,
        'pv_count_freshman': pv_count_freshman,
        'pv_count_sophomore': pv_count_sophomore,
        'pv_count_junior': pv_count_junior,
        'pv_count_senior': pv_count_senior,
        'pv_count_other': pv_count_other,
        'pse_count_freshman': pse_count_freshman,
        'pse_count_sophomore': pse_count_sophomore,
        'pse_count_junior': pse_count_junior,
        'pse_count_senior': pse_count_senior,
        'pse_count_other': pse_count_other,
        'pre_count_freshman': pre_count_freshman,
        'pre_count_sophomore': pre_count_sophomore,
        'pre_count_junior': pre_count_junior,
        'pre_count_senior': pre_count_senior,
        'pre_count_other': pre_count_other,
        'total_count_freshman': total_count_freshman,
        'total_count_sophomore': total_count_sophomore,
        'total_count_junior': total_count_junior,
        'total_count_senior': total_count_senior,
        'total_count_other': total_count_other,
        'total_threat': total_threat,
        'total_coping': total_coping,
        'total_number': total_number,
        'avg_avg_age': avg_avg_age,
        'final_pred': final_pred,
        'now': now,
        # perceived severity
        'ps_number': ps_number,
        'ps_avg_age': ps_avg_age,
        'ps_pred_value': ps_pred_value,
        'ps_count_threat': ps_count_threat,
        'ps_count_coping': ps_count_coping,
        # perceived vulnerability
        'pv_number': pv_number,
        'pv_avg_age': pv_avg_age,
        'pv_pred_value': pv_pred_value,
        'pv_count_threat': pv_count_threat,
        'pv_count_coping': pv_count_coping,
        # perceived self-efficacy
        'pse_number': pse_number,
        'pse_avg_age': pse_avg_age,
        'pse_pred_value': pse_pred_value,
        'pse_count_threat': pse_count_threat,
        'pse_count_coping': pse_count_coping,
        # perceived response efficacy
        'pre_number': pre_number,
        'pre_avg_age': pre_avg_age,
        'pre_pred_value': pre_pred_value,
        'pre_count_threat': pre_count_threat,
        'pre_count_coping': pre_count_coping,
    }
    return render(request, 'datasets.html', context)


# SECTION B
def perceived_severity(request):
    if request.method == 'POST':
        form = PerceivedSeverityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perceived_severity_results')
    else:
        form = PerceivedSeverityForm()
    context = {
        'form': form
    }
    return render(request, 'perceived_severity.html', context)


# SECTION C
def perceived_vulnerability(request):
    if request.method == 'POST':
        form = PerceivedVulnerabilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perceived_vulnerability_results')
    else:
        form = PerceivedVulnerabilityForm()
    context = {
        'form': form
    }
    return render(request, 'perceived_vulnerability.html', context)


# SECTION D
def perceived_response_efficacy(request):
    if request.method == 'POST':
        form = PerceivedResponseEfficacyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perceived_response_efficacy_results')
    else:
        form = PerceivedResponseEfficacyForm()
    context = {
        'form': form
    }
    return render(request, 'perceived_response_efficacy.html', context)


# SECTION E
def perceived_self_efficacy(request):
    if request.method == 'POST':
        form = PerceivedSelfEfficacyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perceived_self_efficacy_results')
    else:
        form = PerceivedSelfEfficacyForm()
    context = {
        'form': form
    }
    return render(request, 'perceived_self_efficacy.html', context)


""" View PMT ML Model Predictions """


# Perceived Severity Results
def perceived_severity_results(request):
    now = datetime.datetime.now()
    predicted_appraisal = PerceivedSeverity.objects.all().order_by('-id')[:5]
    ps = PerceivedSeverity.objects.all()
    ps_number = ps.count()
    ps_age = sum(ps.values_list('age', flat=True))
    try:
        ps_avg_age = int(ps_age / ps_number)
    except ZeroDivisionError:
        ps_avg_age = 0

    ps_count_threat = PerceivedSeverity.objects.filter(predictions="['THREAT']").count()
    ps_count_coping = PerceivedSeverity.objects.filter(predictions="['COPING']").count()
    if ps_count_threat > ps_count_coping:
        ps_pred_value = 'THREAT APPRAISAL'
    elif ps_count_coping > ps_count_threat:
        ps_pred_value = 'COPING APPRAISAL'
    else:
        ps_pred_value = 'UNCATEGORIZED YET'

    context = {
        'now': now,
        'predicted_appraisal': predicted_appraisal,
        'ps_number': ps_number,
        'ps_avg_age': ps_avg_age,
        'ps_pred_value': ps_pred_value,
        'ps_count_threat': ps_count_threat,
        'ps_count_coping': ps_count_coping,
    }
    return render(request, 'perceived_severity_results.html', context)


# perceived vulnerability results
def perceived_vulnerability_results(request):
    now = datetime.datetime.now()
    predicted_appraisal = PerceivedVulnerability.objects.all().order_by('-id')[:10]
    pv = PerceivedVulnerability.objects.all()
    pv_number = pv.count()
    pv_age = sum(pv.values_list('age', flat=True))
    try:
        pv_avg_age = int(pv_age / pv_number)
    except ZeroDivisionError:
        pv_avg_age = 0

    pv_count_threat = PerceivedVulnerability.objects.filter(predictions="['THREAT']").count()
    pv_count_coping = PerceivedVulnerability.objects.filter(predictions="['COPING']").count()
    if pv_count_threat > pv_count_coping:
        pv_pred_value = 'THREAT APPRAISAL'
    elif pv_count_coping > pv_count_threat:
        pv_pred_value = 'COPING APPRAISAL'
    else:
        pv_pred_value = 'UNCATEGORIZED YET'
    context = {
        'now': now,
        'predicted_appraisal': predicted_appraisal,
        'pv_number': pv_number,
        'pv_avg_age': pv_avg_age,
        'pv_pred_value': pv_pred_value,
        'pv_count_threat': pv_count_threat,
        'pv_count_coping': pv_count_coping,
    }
    return render(request, 'perceived_vulnerability_results.html', context)


# perceived response efficacy results
def perceived_response_efficacy_results(request):
    now = datetime.datetime.now()
    predicted_appraisal = PerceivedResponseEfficacy.objects.all().order_by('-id')[:5]
    pre = PerceivedResponseEfficacy.objects.all()
    pre_number = pre.count()
    pre_age = sum(pre.values_list('age', flat=True))
    try:
        pre_avg_age = int(pre_age / pre_number)
    except ZeroDivisionError:
        pre_avg_age = 0

    pre_count_threat = PerceivedResponseEfficacy.objects.filter(predictions="['THREAT']").count()
    pre_count_coping = PerceivedResponseEfficacy.objects.filter(predictions="['COPING']").count()
    if pre_count_threat > pre_count_coping:
        pre_pred_value = 'THREAT APPRAISAL'
    elif pre_count_coping > pre_count_threat:
        pre_pred_value = 'COPING APPRAISAL'
    else:
        pre_pred_value = 'UNCATEGORIZED YET'
    context = {
        'now': now,
        'predicted_appraisal': predicted_appraisal,
        'pre_number': pre_number,
        'pre_avg_age': pre_avg_age,
        'pre_pred_value': pre_pred_value,
        'pre_count_threat': pre_count_threat,
        'pre_count_coping': pre_count_coping
    }
    return render(request, 'perceived_response_efficacy_results.html', context)


# perceived self-efficacy results
def perceived_self_efficacy_results(request):
    now = datetime.datetime.now()
    predicted_appraisal = PerceivedSelfEfficacy.objects.all().order_by('-id')[:5]
    pse = PerceivedSelfEfficacy.objects.all()
    pse_number = pse.count()
    pse_age = sum(pse.values_list('age', flat=True))
    try:
        pse_avg_age = int(pse_age / pse_number)
    except ZeroDivisionError:
        pse_avg_age = 0

    pse_count_threat = PerceivedSelfEfficacy.objects.filter(predictions="['THREAT']").count()
    pse_count_coping = PerceivedSelfEfficacy.objects.filter(predictions="['COPING']").count()
    if pse_count_threat > pse_count_coping:
        pse_pred_value = 'THREAT APPRAISAL'
    elif pse_count_coping > pse_count_threat:
        pse_pred_value = 'COPING APPRAISAL'
    else:
        pse_pred_value = 'UNCATEGORIZED YET'

    context = {
        'now': now,
        'predicted_appraisal': predicted_appraisal,
        'pse_number': pse_number,
        'pse_avg_age': pse_avg_age,
        'pse_pred_value': pse_pred_value,
        'pse_count_threat': pse_count_threat,
        'pse_count_coping': pse_count_coping
    }
    return render(request, 'perceived_self_efficacy_results.html', context)
