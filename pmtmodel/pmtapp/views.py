from django.shortcuts import render, redirect
from .models import DemographicInformation
from .models import PerceivedSeverity
from .models import PerceivedVulnerability
from .models import PerceivedResponseEfficacy
from .models import PerceivedSelfEfficacy
from .models import PerceivedPreventionAndResponseCost
from .models import SocialNetworkSecurity
from .forms import DemographicInformationForm
from .forms import PerceivedSeverityForm
from .forms import PerceivedVulnerabilityForm
from .forms import PerceivedResponseEfficacyForm
from .forms import PerceivedSelfEfficacyForm
from .forms import PerceivedPreventionAndResponseCostForm
from .forms import SocialNetworkSecurityForm


def home(request):
    return render(request, 'home.html')


def datasets(request):
    return render(request, 'datasets.html')


# SECTION A.
def demographic_information(request):
    if request.method == 'POST':
        form = DemographicInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('results')
    else:
        form = DemographicInformationForm()
    context = {
        'form': form
    }
    return render(request, 'demographic_information.html', context)


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


# SECTION F
def perceived_prevention_response_cost(request):
    if request.method == 'POST':
        form = PerceivedPreventionAndResponseCostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perceived_prevention_response_cost_results')
    else:
        form = PerceivedPreventionAndResponseCostForm()
    context = {
        'form': form
    }
    return render(request, 'perceived_prevention_response_cost.html', context)


# SECTION G
def intended_user_behaviour(request):
    if request.method == 'POST':
        form = SocialNetworkSecurityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('intended_user_behaviour_results')
    else:
        form = SocialNetworkSecurityForm()
    context = {
        'form': form
    }
    return render(request, 'intended_user_behaviour.html', context)


""" View PMT ML Model Predictions """


# Demographic Information Prediction
def results(request):
    predicted_appraisal = DemographicInformation.objects.all().order_by('-id')[:10]
    context = {
        'predicted_appraisal': predicted_appraisal
    }
    return render(request, 'results.html', context)


# Perceived Severity Results
def perceived_severity_results(request):
    predicted_appraisal = PerceivedSeverity.objects.all().order_by('-id')[:10]
    context = {
        'predicted_appraisal': predicted_appraisal
    }
    return render(request, 'perceived_severity_results.html', context)


# perceived vulnerability results
def perceived_vulnerability_results(request):
    predicted_appraisal = PerceivedVulnerability.objects.all().order_by('-id')[:10]
    context = {
        'predicted_appraisal': predicted_appraisal
    }
    return render(request, 'perceived_vulnerability_results.html', context)


# perceived response efficacy results
def perceived_response_efficacy_results(request):
    predicted_appraisal = PerceivedResponseEfficacy.objects.all().order_by('-id')[:10]
    context = {
        'predicted_appraisal': predicted_appraisal
    }
    return render(request, 'perceived_response_efficacy_results.html', context)


# perceived self-efficacy results
def perceived_self_efficacy_results(request):
    predicted_appraisal = PerceivedSelfEfficacy.objects.all().order_by('-id')[:10]
    context = {
        'predicted_appraisal': predicted_appraisal
    }
    return render(request, 'perceived_self_efficacy_results.html', context)


# Perceived prevention & response cost prediction
def perceived_prevention_response_cost_results(request):
    predicted_appraisal = PerceivedPreventionAndResponseCost.objects.all().order_by('-id')[:10]
    context = {
        'predicted_appraisal': predicted_appraisal
    }
    return render(request, 'perceived_prevention_response_cost_results.html', context)


#   Intended User Behavior results prediction
def intended_user_behaviour_results(request):
    predicted_appraisal = SocialNetworkSecurity.objects.all().order_by('-id')[:10]
    context = {
        'predicted_appraisal': predicted_appraisal
    }
    return render(request, 'intended_user_behaviour_results.html', context)
