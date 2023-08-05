from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import DemographicInformation, PerceivedSeverity, PerceivedVulnerability, PerceivedResponseEfficacy, \
    PerceivedSelfEfficacy, PerceivedPreventionAndResponseCost, SocialNetworkSecurity
from .forms import DemographicInformationForm, PerceivedSeverityForm, PerceivedVulnerabilityForm, \
    PerceivedResponseEfficacyForm, PerceivedSelfEfficacyForm, PerceivedPreventionAndResponseCostForm, \
    SocialNetworkSecurityForm
from django.contrib import messages
import csv
from django.conf import settings
import os
import joblib

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

""" ml model """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn import metrics
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import numpy as np
import warnings


def home(request):
    return render(request, 'home.html')


def datasets(request):
    # pv = PerceivedVulnerability.objects.all()
    # di = DemographicInformation.objects.all()
    # pse = PerceivedSelfEfficacy.objects.all()
    # pre = PerceivedResponseEfficacy.objects.all()
    # pprs = PerceivedPreventionAndResponseCost.objects.all()
    # sns = SocialNetworkSecurity
    # context = {
    #     'ps': ps,
    #     # 'pv': pv,
    #     # 'di': di,
    #     # 'pse': pse,
    #     # 'pre': pre,
    #     # 'pprs': pprs,
    #     # 'sns': sns
    # }
    return render(request, 'datasets.html')


def ps_csv(request):
    ps = PerceivedSeverity.objects.all()
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=perceived_severity.csv'
    writer = csv.writer(response)
    writer.writerow(
        ['potential_breach_consequences', 'impact_of_info', 'substantial_harm_by_breaches', 's_media_threats_concern',
         'negative_impacts_breaches', 'info_sharing_risks', 'serious_s_media_security', 'substantial_data_breaches',
         'high_network_severity', 's_media_negative_consequences'])
    ps_fields = ps.values_list('potential_breach_consequences', 'impact_of_info', 'substantial_harm_by_breaches',
                               's_media_threats_concern', 'negative_impacts_breaches', 'info_sharing_risks',
                               'serious_s_media_security', 'substantial_data_breaches', 'high_network_severity',
                               's_media_negative_consequences')

    for data in ps_fields:
        writer.writerow(data)
    return response


def pv_csv(request):
    pv = PerceivedVulnerability.objects.all()
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=perceived_vulnerability.csv'
    writer = csv.writer(response)
    writer.writerow(
        ['security_breach_likelyness', 'vulnerable_security_breach', 'info_sharing_risk_concern', 'protect_info_online',
         'online_potential_threats', 'update_privacy_settings', 'likely_2FA_authentication', 'concerned_info_breaches',
         'online_info_privacy', 'report_suspicious_activity'])
    pv_fields = pv.values_list('security_breach_likelyness', 'vulnerable_security_breach', 'info_sharing_risk_concern',
                               'protect_info_online',
                               'online_potential_threats', 'update_privacy_settings', 'likely_2FA_authentication',
                               'concerned_info_breaches',
                               'online_info_privacy', 'report_suspicious_activity')

    for data in pv_fields:
        writer.writerow(data)
    return response


def pre_csv(request):
    pre = PerceivedResponseEfficacy.objects.all()
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=perceived_response_efficacy.csv'
    writer = csv.writer(response)
    writer.writerow(
        ['effective_security_measures', 'privacy_settings_protecting_info', 'strong_password_security',
         'regular_security_updates',
         'cautious_link_clicking', 'info_sharing_security', 'minimize_suspicious_individuals', 'backing_up_data',
         'privacy_security_updates', 'sharing_info_security_reduction'])
    pre_fields = pre.values_list('effective_security_measures', 'privacy_settings_protecting_info',
                                 'strong_password_security', 'regular_security_updates',
                                 'cautious_link_clicking', 'info_sharing_security', 'minimize_suspicious_individuals',
                                 'backing_up_data',
                                 'privacy_security_updates', 'sharing_info_security_reduction')

    for data in pre_fields:
        writer.writerow(data)
    return response


def pse_csv(request):
    pse = PerceivedSelfEfficacy.objects.all()
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=perceived_self_efficacy.csv'
    writer = csv.writer(response)
    writer.writerow(
        ['effective_security_knowledge', 'security_threats_avoidance', 'privacy_setting_usage',
         'suspicious_links_avoidance',
         'suspicious_individuals_avoidance', 'antivirus_usage_knowledge', 'managing_social_connections',
         'privacy_issues_identification',
         'software_updates_security', 'accounts_strong_passwords'])
    pse_fields = pse.values_list('effective_security_knowledge', 'security_threats_avoidance', 'privacy_setting_usage',
                                 'suspicious_links_avoidance',
                                 'suspicious_individuals_avoidance', 'antivirus_usage_knowledge',
                                 'managing_social_connections', 'privacy_issues_identification',
                                 'software_updates_security', 'accounts_strong_passwords')

    for data in pse_fields:
        writer.writerow(data)
    return response


def pprc_csv(request):
    pprc = PerceivedPreventionAndResponseCost.objects.all()
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=perceived_prevention_response_cost.csv'
    writer = csv.writer(response)
    writer.writerow(
        ['security_implementation_efforts_high', 'security_financial_enhancing_high', 'security_efforts_practices_high',
         'security_inconvenience_outweighs_benefits',
         'security_loss_functionality_undesirable', 'security_incidence_response_overwhelming',
         'security_financial_cost_reasonable',
         'security_updates_time_and_efforts_reasonable',
         'security_potential_risks_outweighs_implementations'])
    pprc_fields = pprc.values_list('security_implementation_efforts_high', 'security_financial_enhancing_high',
                                   'security_efforts_practices_high',
                                   'security_inconvenience_outweighs_benefits',
                                   'security_loss_functionality_undesirable',
                                   'security_incidence_response_overwhelming', 'security_financial_cost_reasonable',
                                   'security_updates_time_and_efforts_reasonable',
                                   'security_potential_risks_outweighs_implementations')

    for data in pprc_fields:
        writer.writerow(data)
    return response


def sns_csv(request):
    sns = SocialNetworkSecurity.objects.all()
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=intended_user_behavior.csv'
    writer = csv.writer(response)
    writer.writerow(
        ['privacy_personal_info_maintenance', 'proactive_personal_info_access_management', 'use_of_security_features',
         'personal_info_risk_consciousness',
         'secure_account_with_regular_updates', 'learn_social_network_security', 'interacting_with_suspicious_accounts',
         'block_report_suspicious_accounts',
         'educate_social_network_security', 'mind_privacy_policies_before_using'])
    sns_fields = sns.values_list('privacy_personal_info_maintenance', 'proactive_personal_info_access_management',
                                 'use_of_security_features',
                                 'personal_info_risk_consciousness',
                                 'secure_account_with_regular_updates', 'learn_social_network_security',
                                 'interacting_with_suspicious_accounts',
                                 'block_report_suspicious_accounts',
                                 'educate_social_network_security', 'mind_privacy_policies_before_using')

    for data in sns_fields:
        writer.writerow(data)
    return response


def di_csv(request):
    di = DemographicInformation.objects.all()
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=demographic_information.csv'
    writer = csv.writer(response)
    writer.writerow(
        ['gender', 'age', 'academic_year',
         'field_of_study',
         'university', 'university_funding', 'mode_of_study',
         's_media_security_knowledge',
         'social_media_usage', 'active_social_platforms', 'average_hours_s_media', 's_media_security_concern',
         'social_media_breaches', 's_media_security_measure', 'privacy_security_education', 's_media_self_protection',
         's_media_privacy_settings_awareness', 'often_review_privacy_settings', 's_media_personal_info_sharing',
         'victim_of_cyberbullying', 's_media_privacy_security_features', 's_media_sensitive_info_sharing',
         's_media_malicious_encounters', 'more_s_media_user_protection', 's_media_privacy_policy_and_TOS',
         'delete_account_due_to_privacy', 's_media_security_education'])
    di_fields = di.values_list('gender', 'age', 'academic_year',
                               'field_of_study',
                               'university', 'university_funding', 'mode_of_study',
                               's_media_security_knowledge',
                               'social_media_usage', 'active_social_platforms', 'average_hours_s_media',
                               's_media_security_concern', 'social_media_breaches', 's_media_security_measure',
                               'privacy_security_education', 's_media_self_protection',
                               's_media_privacy_settings_awareness', 'often_review_privacy_settings',
                               's_media_personal_info_sharing', 'victim_of_cyberbullying',
                               's_media_privacy_security_features', 's_media_sensitive_info_sharing',
                               's_media_malicious_encounters', 'more_s_media_user_protection',
                               's_media_privacy_policy_and_TOS', 'delete_account_due_to_privacy',
                               's_media_security_education')

    for data in di_fields:
        writer.writerow(data)
    return response


# SECTION B
def perceived_severity(request):
    form = PerceivedSeverityForm()
    if request.method == 'POST':
        form = PerceivedSeverityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Submitted Successfully.')
            # model
            warnings.filterwarnings("ignore")

            model = joblib.load('static/ml_efficacy_pmt.joblib')

            # Get the input data from the form
            feature1 = float(request.POST.get('potential_breach_consequences'))
            feature2 = float(request.POST.get('impact_of_info'))
            feature3 = float(request.POST.get('substantial_harm_by_breaches'))
            feature4 = float(request.POST.get('s_media_threats_concern'))
            feature5 = float(request.POST.get('negative_impacts_breaches'))
            feature6 = float(request.POST.get('info_sharing_risks'))
            feature7 = float(request.POST.get('serious_s_media_security'))
            feature8 = float(request.POST.get('substantial_data_breaches'))
            feature9 = float(request.POST.get('high_network_severity'))
            feature10 = float(request.POST.get('s_media_negative_consequences'))

            # Prepare the input data for prediction
            input_data = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7,
                           feature8, feature9, feature10]]  # Create a list of lists if multiple samples

            # make predictions using linear regression
            predict = model.predict(input_data)

            # Pass the predictions to the template for rendering
            context = {
                'predict': predict,
            }
            return render(request, 'perceived_severity_results.html', context)
        else:
            messages.error(request, 'FAILED! Something went wrong.')
            context = {
                'form': form
            }
            return render(request, 'perceived_severity.html', context)
    context = {
        'form': form,
        # 'value': value
    }
    return render(request, 'perceived_severity.html', context)


# SECTION C
def perceived_vulnerability(request):
    form = PerceivedVulnerabilityForm()
    if request.method == 'POST':
        form = PerceivedVulnerabilityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Submitted Successfully.')

            # model
            model = joblib.load('static/ml_efficacy_pmt.joblib')

            # Get the input data from the form
            feature1 = float(request.POST.get('security_breach_likelyness'))
            feature2 = float(request.POST.get('vulnerable_security_breach'))
            feature3 = float(request.POST.get('info_sharing_risk_concern'))
            feature4 = float(request.POST.get('protect_info_online'))
            feature5 = float(request.POST.get('online_potential_threats'))
            feature6 = float(request.POST.get('update_privacy_settings'))
            feature7 = float(request.POST.get('likely_2FA_authentication'))
            feature8 = float(request.POST.get('concerned_info_breaches'))
            feature9 = float(request.POST.get('online_info_privacy'))
            feature10 = float(request.POST.get('report_suspicious_activity'))

            # Prepare the input data for prediction
            input_data = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8,
                           feature9, feature10]]  # Create a list of lists if multiple samples

            # make predictions using linear regression
            predict = model.predict(input_data)

            # Pass the predictions to the template for rendering
            context = {
                'predict': predict,
            }
            return render(request, 'perceived_vulnerability_results.html', context)
        else:
            messages.error(request, 'FAILED! Something went wrong.')
            context = {
                'form': form
            }
            return render(request, 'perceived_vulnerability.html', context)
    context = {
        'form': form
    }
    return render(request, 'perceived_vulnerability.html', context)


# SECTION D
def perceived_response_efficacy(request):
    form = PerceivedResponseEfficacyForm()
    if request.method == 'POST':
        form = PerceivedResponseEfficacyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Submitted Successfully.')

            # model
            model = joblib.load('static/ml_efficacy_pmt.joblib')

            # Get the input data from the form
            feature1 = float(request.POST.get('effective_security_measures'))
            feature2 = float(request.POST.get('privacy_settings_protecting_info'))
            feature3 = float(request.POST.get('strong_password_security'))
            feature4 = float(request.POST.get('regular_security_updates'))
            feature5 = float(request.POST.get('cautious_link_clicking'))
            feature6 = float(request.POST.get('info_sharing_security'))
            feature7 = float(request.POST.get('minimize_suspicious_individuals'))
            feature8 = float(request.POST.get('backing_up_data'))
            feature9 = float(request.POST.get('privacy_security_updates'))
            feature10 = float(request.POST.get('sharing_info_security_reduction'))

            # Prepare the input data for prediction
            input_data = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8,
                           feature9, feature10]]  # Create a list of lists if multiple samples

            # make predictions using linear regression
            predict = model.predict(input_data)

            # Pass the predictions to the template for rendering
            context = {
                'predict': predict
            }
            return render(request, 'perceived_response_efficacy_results.html', context)
        else:
            messages.error(request, 'FAILED! Something went wrong.')
            context = {
                'form': form
            }
            return render(request, 'perceived_response_efficacy.html', context)
    context = {
        'form': form
    }
    return render(request, 'perceived_response_efficacy.html', context)


# SECTION E
def perceived_self_efficacy(request):
    form = PerceivedSelfEfficacyForm()
    if request.method == 'POST':
        form = PerceivedSelfEfficacyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Submitted Successfully.')

            # model
            model = joblib.load('static/ml_efficacy_pmt.joblib')

            # Get the input data from the form
            feature1 = float(request.POST.get('effective_security_knowledge'))
            feature2 = float(request.POST.get('security_threats_avoidance'))
            feature3 = float(request.POST.get('privacy_setting_usage'))
            feature4 = float(request.POST.get('suspicious_links_avoidance'))
            feature5 = float(request.POST.get('suspicious_individuals_avoidance'))
            feature6 = float(request.POST.get('antivirus_usage_knowledge'))
            feature7 = float(request.POST.get('managing_social_connections'))
            feature8 = float(request.POST.get('privacy_issues_identification'))
            feature9 = float(request.POST.get('software_updates_security'))
            feature10 = float(request.POST.get('accounts_strong_passwords'))

            # Prepare the input data for prediction
            input_data = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8,
                           feature9, feature10]]  # Create a list of lists if multiple samples

            # make predictions using linear regression
            predict = model.predict(input_data)

            # Pass the predictions to the template for rendering
            context = {
                'predict': predict
            }
            return render(request, 'perceived_self_efficacy_results.html', context)
        else:
            messages.error(request, 'FAILED! Something went wrong.')
            context = {
                'form': form
            }
            return render(request, 'perceived_self_efficacy.html', context)
    context = {
        'form': form
    }
    return render(request, 'perceived_self_efficacy.html', context)


# SECTION F
def perceived_prevention_response_cost(request):
    form = PerceivedPreventionAndResponseCostForm()
    if request.method == 'POST':
        form = PerceivedPreventionAndResponseCostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Submitted Successfully.')

            # model
            model = joblib.load('static/ml_efficacy_pmt.joblib')

            # Get the input data from the form
            feature1 = float(request.POST.get('security_implementation_efforts_high'))
            feature2 = float(request.POST.get('security_financial_enhancing_high'))
            feature3 = float(request.POST.get('security_efforts_practices_high'))
            feature4 = float(request.POST.get('security_inconvenience_outweighs_benefits'))
            feature5 = float(request.POST.get('security_loss_functionality_undesirable'))
            feature6 = float(request.POST.get('security_incidence_response_overwhelming'))
            feature7 = float(request.POST.get('security_financial_cost_reasonable'))
            feature8 = float(request.POST.get('security_updates_time_and_efforts_reasonable'))
            feature9 = float(request.POST.get('security_potential_risks_outweighs_implementations'))
            feature10 = float(request.POST.get('security_potential_risks_outweighs_implementation'))
            # Prepare the input data for prediction
            input_data = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7,
                           feature8, feature9, feature10]]  # Create a list of lists if multiple samples

            # make predictions using linear regression
            predict = model.predict(input_data)

            # Pass the predictions to the template for rendering
            context = {
               'predict': predict
            }
            return render(request, 'perceived_prevention_response_cost_results.html', context)
        else:
            messages.error(request, 'FAILED! Something went wrong.')
            context = {
                'form': form
            }
            return render(request, 'perceived_prevention_response_cost.html', context)
    context = {
        'form': form
    }
    return render(request, 'perceived_prevention_response_cost.html', context)


# SECTION G
def intended_user_behaviour(request):
    form = SocialNetworkSecurityForm()
    if request.method == 'POST':
        form = SocialNetworkSecurityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Submitted Successfully.')

            # model
            model = joblib.load('static/ml_efficacy_pmt.joblib')

            # Get the input data from the form
            feature1 = float(request.POST.get('privacy_personal_info_maintenance'))
            feature2 = float(request.POST.get('proactive_personal_info_access_management'))
            feature3 = float(request.POST.get('use_of_security_features'))
            feature4 = float(request.POST.get('personal_info_risk_consciousness'))
            feature5 = float(request.POST.get('secure_account_with_regular_updates'))
            feature6 = float(request.POST.get('learn_social_network_security'))
            feature7 = float(request.POST.get('interacting_with_suspicious_accounts'))
            feature8 = float(request.POST.get('block_report_suspicious_accounts'))
            feature9 = float(request.POST.get('educate_social_network_security'))
            feature10 = float(request.POST.get('mind_privacy_policies_before_using'))

            # Prepare the input data for prediction
            input_data = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7,
                           feature8, feature9, feature10]]  # Create a list of lists if multiple samples

            # make predictions using linear regression
            predict = model.predict(input_data)

            # Pass the predictions to the template for rendering
            context = {
                'predict': predict
            }
            return render(request, 'intended_user_behaviour_results.html', context)
        else:
            messages.error(request, 'FAILED! Something went wrong.')
            context = {
                'form': form
            }
            return render(request, 'intended_user_behaviour.html', context)
    context = {
        'form': form
    }
    return render(request, 'intended_user_behaviour.html', context)


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


# view Results
def results(request):
    predicted_appraisal = DemographicInformation.objects.all().order_by('-id')[:10]
    context = {
        'predicted_appraisal': predicted_appraisal
    }
    return render(request, 'results.html', context)


# Perceived Severity Results
def perceived_severity_results(request):
    return render(request, 'perceived_severity_results.html')


# perceived vulnerability results
def perceived_vulnerability_results(request):
    return render(request, 'perceived_vulnerability_results.html')


# perceived response efficacy results
def perceived_response_efficacy_results(request):
    return render(request, 'perceived_response_efficacy_results.html')


# perceived self-efficacy results
def perceived_self_efficacy_results(request):
    return render(request, 'perceived_self_efficacy_results.html')


# perceived prevention response cost results
def perceived_prevention_response_cost_results(request):
    return render(request, 'perceived_prevention_response_cost_results.html')


# social network security
def intended_user_behaviour_results(request):
    return render(request, 'intended_user_behaviour_results.html')
