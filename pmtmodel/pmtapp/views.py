from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DemographicInformation, PerceivedSeverity, PerceivedVulnerability, PerceivedResponseEfficacy, \
    PerceivedSelfEfficacy, PerceivedPreventionAndResponseCost, SocialNetworkSecurity
from .forms import DemographicInformationForm, PerceivedSeverityForm, PerceivedVulnerabilityForm, \
    PerceivedResponseEfficacyForm, PerceivedSelfEfficacyForm, PerceivedPreventionAndResponseCostForm, \
    SocialNetworkSecurityForm
from django.contrib import messages
import csv
from django.conf import settings
import os

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
    ps = PerceivedSeverity.objects.all()
    context = {
        'ps': ps
    }
    return render(request, 'datasets.html', context)


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
            data = PerceivedSeverity.objects.all()
            file_path = os.path.join(settings.STATIC_ROOT, 'perceived_severity.csv')

            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(
                    ['Breach Consequences', 'Info Impact', 'Breach Harms', 'Threats Concern', 'Breach Impacts',
                     'Info Risks',
                     'Social Security', 'Substantial Breaches', 'Network Security', 'Negative Consequences'])

                for item in data:
                    writer.writerow(
                        [item.potential_breach_consequences, item.impact_of_info, item.substantial_harm_by_breaches,
                         item.s_media_threats_concern, item.negative_impacts_breaches, item.info_sharing_risks,
                         item.serious_s_media_security, item.substantial_data_breaches, item.high_network_severity,
                         item.s_media_negative_consequences])

            data_frame = pd.read_csv('static/perceived_severity.csv')

            # Extract the features and target variables from the data
            y = data_frame['Negative Consequences']
            X = data_frame.drop('Negative Consequences', axis=1)

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train model
            """ Linear Regression """

            l_reg_model = LinearRegression()
            l_reg_model.fit(X_train, y_train)

            # train model to make prediction
            y_l_reg_train_pred = l_reg_model.predict(X_train)
            y_l_reg_test_pred = l_reg_model.predict(X_test)

            # Evaluate Model Performance
            l_reg_train_mse = mean_squared_error(y_train, y_l_reg_train_pred)
            l_reg_train_r2 = r2_score(y_train, y_l_reg_train_pred)
            l_reg_test_mse = mean_squared_error(y_test, y_l_reg_test_pred)
            l_reg_test_r2 = r2_score(y_test, y_l_reg_test_pred)

            """ Random Forest """

            # Training Model
            r_frt_model = RandomForestRegressor(max_depth=2, random_state=100)
            r_frt_model.fit(X_train, y_train)
            y_r_frt_train_pred = r_frt_model.predict(X_train)
            y_r_frt_test_pred = r_frt_model.predict(X_test)

            # Evaluate model performance
            r_frt_train_mse = mean_squared_error(y_train, y_r_frt_train_pred)
            r_frt_train_r2 = r2_score(y_train, y_r_frt_train_pred)
            r_frt_test_mse = mean_squared_error(y_test, y_r_frt_test_pred)
            r_frt_test_r2 = r2_score(y_test, y_r_frt_test_pred)

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
            # feature10 = float(request.POST.get('report_suspicious_activity'))

            # Prepare the input data for prediction
            input_data = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7,
                           feature8, feature9]]  # Create a list of lists if multiple samples

            # make predictions using linear regression
            y_l_reg_test_pred = l_reg_model.predict(input_data)

            # Make predictions using random forest
            y_r_frt_test_pred = r_frt_model.predict(input_data)

            # Evaluate model performance
            # r_frt_predict_mse = mean_squared_error(y_train, y_r_frt_test_pred)
            # r_frt_predict_r2 = r2_score(y_train, y_r_frt_test_pred)
            # r_frt_test_mse = mean_squared_error(y_test, ret)
            # r_frt_test_r2 = r2_score(y_test, ret)

            # Pass the predictions to the template for rendering
            context = {
                # linear regression train & test
                'l_reg_train_mse': l_reg_train_mse,
                'l_reg_train_r2': l_reg_train_r2,
                'l_reg_test_mse': l_reg_test_mse,
                'l_reg_test_r2': l_reg_test_r2,
                # linear regression predict
                'y_l_reg_test_pred': y_l_reg_test_pred,
                # random forest train & test
                'r_frt_train_mse': r_frt_train_mse,
                'r_frt_train_r2': r_frt_train_r2,
                'r_frt_test_mse': r_frt_test_mse,
                'r_frt_test_r2': r_frt_test_r2,
                # random forest predict
                'y_r_frt_test_pred': y_r_frt_test_pred
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
            warnings.filterwarnings("ignore")
            # Retrieve the data from your Django model
            data = PerceivedVulnerability.objects.all()
            file_path = os.path.join(settings.STATIC_ROOT, 'perceived_vulnerability.csv')

            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(
                    ['Breach Consequences', 'Info Impact', 'Threats Concern', 'Breach Impacts',
                     'Info Risks',
                     'Social Security', 'Substantial Breaches', 'Mjampo', 'Network Security', 'Negative'])

                for item in data:
                    writer.writerow(
                        [item.security_breach_likelyness, item.vulnerable_security_breach, item.info_sharing_risk_concern,
                         item.protect_info_online, item.online_potential_threats, item.update_privacy_settings,
                         item.likely_2FA_authentication, item.concerned_info_breaches, item.online_info_privacy, item.report_suspicious_activity])

            data_frame = pd.read_csv('static/perceived_vulnerability.csv')
            # Extract the features and target variables from the data
            y = data_frame['Negative']
            X = data_frame.drop('Negative', axis=1)

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train model
            """ Linear Regression """

            l_reg_model = LinearRegression()
            l_reg_model.fit(X_train, y_train)

            # train model to make prediction
            y_l_reg_train_pred = l_reg_model.predict(X_train)
            y_l_reg_test_pred = l_reg_model.predict(X_test)

            # Evaluate Model Performance
            l_reg_train_mse = mean_squared_error(y_train, y_l_reg_train_pred)
            l_reg_train_r2 = r2_score(y_train, y_l_reg_train_pred)
            l_reg_test_mse = mean_squared_error(y_test, y_l_reg_test_pred)
            l_reg_test_r2 = r2_score(y_test, y_l_reg_test_pred)

            """ Random Forest """

            # Training Model
            r_frt_model = RandomForestRegressor(max_depth=2, random_state=100)
            r_frt_model.fit(X_train, y_train)
            y_r_frt_train_pred = r_frt_model.predict(X_train)
            y_r_frt_test_pred = r_frt_model.predict(X_test)

            # Evaluate model performance
            r_frt_train_mse = mean_squared_error(y_train, y_r_frt_train_pred)
            r_frt_train_r2 = r2_score(y_train, y_r_frt_train_pred)
            r_frt_test_mse = mean_squared_error(y_test, y_r_frt_test_pred)
            r_frt_test_r2 = r2_score(y_test, y_r_frt_test_pred)

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
            # feature10 = float(request.POST.get('report_suspicious_activity'))

            # Prepare the input data for prediction
            input_data = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9]]  # Create a list of lists if multiple samples

            # make predictions using linear regression
            y_l_reg_test_pred = l_reg_model.predict(input_data)

            # Make predictions using random forest
            y_r_frt_test_pred = r_frt_model.predict(input_data)

            # Evaluate model performance
            # r_frt_predict_mse = mean_squared_error(y_train, y_r_frt_test_pred)
            # r_frt_predict_r2 = r2_score(y_train, y_r_frt_test_pred)
            # r_frt_test_mse = mean_squared_error(y_test, ret)
            # r_frt_test_r2 = r2_score(y_test, ret)

            # Pass the predictions to the template for rendering
            context = {
                # linear regression train & test
                'l_reg_train_mse': l_reg_train_mse,
                'l_reg_train_r2': l_reg_train_r2,
                'l_reg_test_mse': l_reg_test_mse,
                'l_reg_test_r2': l_reg_test_r2,
                # linear regression predict
                'y_l_reg_test_pred': y_l_reg_test_pred,
                # random forest train & test
                'r_frt_train_mse': r_frt_train_mse,
                'r_frt_train_r2': r_frt_train_r2,
                'r_frt_test_mse': r_frt_test_mse,
                'r_frt_test_r2': r_frt_test_r2,
                # random forest predict
                'y_r_frt_test_pred': y_r_frt_test_pred
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
            warnings.filterwarnings("ignore")
            data = PerceivedResponseEfficacy.objects.all()
            file_path = os.path.join(settings.STATIC_ROOT, 'perceived_response_efficacy.csv')

            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(
                    ['Security', 'Settings', 'Password', 'Updates', 'Links', 'Sharing',
                     'Suspicious', 'Backup', 'Privacy', 'Reduction'])

                for item in data:
                    writer.writerow(
                        [item.effective_security_measures, item.privacy_settings_protecting_info, item.strong_password_security,
                         item.regular_security_updates, item.cautious_link_clicking, item.info_sharing_security,
                         item.minimize_suspicious_individuals, item.backing_up_data, item.privacy_security_updates,
                         item.sharing_info_security_reduction])

            data_frame = pd.read_csv('static/perceived_response_efficacy.csv')
            # Extract the features and target variables from the data
            y = data_frame['Reduction']
            X = data_frame.drop('Reduction', axis=1)

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train model
            """ Linear Regression """

            l_reg_model = LinearRegression()
            l_reg_model.fit(X_train, y_train)

            # train model to make prediction
            y_l_reg_train_pred = l_reg_model.predict(X_train)
            y_l_reg_test_pred = l_reg_model.predict(X_test)

            # Evaluate Model Performance
            l_reg_train_mse = mean_squared_error(y_train, y_l_reg_train_pred)
            l_reg_train_r2 = r2_score(y_train, y_l_reg_train_pred)
            l_reg_test_mse = mean_squared_error(y_test, y_l_reg_test_pred)
            l_reg_test_r2 = r2_score(y_test, y_l_reg_test_pred)

            """ Random Forest """

            # Training Model
            r_frt_model = RandomForestRegressor(max_depth=2, random_state=100)
            r_frt_model.fit(X_train, y_train)
            y_r_frt_train_pred = r_frt_model.predict(X_train)
            y_r_frt_test_pred = r_frt_model.predict(X_test)

            # Evaluate model performance
            r_frt_train_mse = mean_squared_error(y_train, y_r_frt_train_pred)
            r_frt_train_r2 = r2_score(y_train, y_r_frt_train_pred)
            r_frt_test_mse = mean_squared_error(y_test, y_r_frt_test_pred)
            r_frt_test_r2 = r2_score(y_test, y_r_frt_test_pred)

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
            # feature10 = float(request.POST.get('report_suspicious_activity'))

            # Prepare the input data for prediction
            input_data = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8,
                           feature9]]  # Create a list of lists if multiple samples

            # make predictions using linear regression
            y_l_reg_test_pred = l_reg_model.predict(input_data)

            # Make predictions using random forest
            y_r_frt_test_pred = r_frt_model.predict(input_data)

            # Evaluate model performance
            # r_frt_predict_mse = mean_squared_error(y_train, y_r_frt_test_pred)
            # r_frt_predict_r2 = r2_score(y_train, y_r_frt_test_pred)
            # r_frt_test_mse = mean_squared_error(y_test, ret)
            # r_frt_test_r2 = r2_score(y_test, ret)

            # Pass the predictions to the template for rendering
            context = {
                # linear regression train & test
                'l_reg_train_mse': l_reg_train_mse,
                'l_reg_train_r2': l_reg_train_r2,
                'l_reg_test_mse': l_reg_test_mse,
                'l_reg_test_r2': l_reg_test_r2,
                # linear regression predict
                'y_l_reg_test_pred': y_l_reg_test_pred,
                # random forest train & test
                'r_frt_train_mse': r_frt_train_mse,
                'r_frt_train_r2': r_frt_train_r2,
                'r_frt_test_mse': r_frt_test_mse,
                'r_frt_test_r2': r_frt_test_r2,
                # random forest predict
                'y_r_frt_test_pred': y_r_frt_test_pred
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
            warnings.filterwarnings("ignore")
            data = PerceivedSelfEfficacy.objects.all()
            file_path = os.path.join(settings.STATIC_ROOT, 'perceived_self_efficacy.csv')

            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(
                    ['Knowledge', 'Threats', 'Privacy', 'Links', 'Individuals', 'Antivirus',
                     'Social', 'Issues', 'Updates', 'Passwords'])

                for item in data:
                    writer.writerow(
                        [item.effective_security_knowledge, item.security_threats_avoidance,
                         item.privacy_setting_usage,
                         item.suspicious_links_avoidance, item.suspicious_individuals_avoidance, item.antivirus_usage_knowledge,
                         item.managing_social_connections, item.privacy_issues_identification, item.software_updates_security,
                         item.accounts_strong_passwords])

            data_frame = pd.read_csv('static/perceived_self_efficacy.csv')
            # Extract the features and target variables from the data
            y = data_frame['Passwords']
            X = data_frame.drop('Passwords', axis=1)

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train model
            """ Linear Regression """

            l_reg_model = LinearRegression()
            l_reg_model.fit(X_train, y_train)

            # train model to make prediction
            y_l_reg_train_pred = l_reg_model.predict(X_train)
            y_l_reg_test_pred = l_reg_model.predict(X_test)

            # Evaluate Model Performance
            l_reg_train_mse = mean_squared_error(y_train, y_l_reg_train_pred)
            l_reg_train_r2 = r2_score(y_train, y_l_reg_train_pred)
            l_reg_test_mse = mean_squared_error(y_test, y_l_reg_test_pred)
            l_reg_test_r2 = r2_score(y_test, y_l_reg_test_pred)

            """ Random Forest """

            # Training Model
            r_frt_model = RandomForestRegressor(max_depth=2, random_state=100)
            r_frt_model.fit(X_train, y_train)
            y_r_frt_train_pred = r_frt_model.predict(X_train)
            y_r_frt_test_pred = r_frt_model.predict(X_test)

            # Evaluate model performance
            r_frt_train_mse = mean_squared_error(y_train, y_r_frt_train_pred)
            r_frt_train_r2 = r2_score(y_train, y_r_frt_train_pred)
            r_frt_test_mse = mean_squared_error(y_test, y_r_frt_test_pred)
            r_frt_test_r2 = r2_score(y_test, y_r_frt_test_pred)

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
            # feature10 = float(request.POST.get('report_suspicious_activity'))

            # Prepare the input data for prediction
            input_data = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8,
                           feature9]]  # Create a list of lists if multiple samples

            # make predictions using linear regression
            y_l_reg_test_pred = l_reg_model.predict(input_data)

            # Make predictions using random forest
            y_r_frt_test_pred = r_frt_model.predict(input_data)

            # Evaluate model performance
            # r_frt_predict_mse = mean_squared_error(y_train, y_r_frt_test_pred)
            # r_frt_predict_r2 = r2_score(y_train, y_r_frt_test_pred)
            # r_frt_test_mse = mean_squared_error(y_test, ret)
            # r_frt_test_r2 = r2_score(y_test, ret)

            # Pass the predictions to the template for rendering
            context = {
                # linear regression train & test
                'l_reg_train_mse': l_reg_train_mse,
                'l_reg_train_r2': l_reg_train_r2,
                'l_reg_test_mse': l_reg_test_mse,
                'l_reg_test_r2': l_reg_test_r2,
                # linear regression predict
                'y_l_reg_test_pred': y_l_reg_test_pred,
                # random forest train & test
                'r_frt_train_mse': r_frt_train_mse,
                'r_frt_train_r2': r_frt_train_r2,
                'r_frt_test_mse': r_frt_test_mse,
                'r_frt_test_r2': r_frt_test_r2,
                # random forest predict
                'y_r_frt_test_pred': y_r_frt_test_pred
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
            warnings.filterwarnings("ignore")
            data = PerceivedPreventionAndResponseCost.objects.all()
            file_path = os.path.join(settings.STATIC_ROOT, 'perceived_prevention_response_cost.csv')

            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(
                    ['Implementation', 'Financial', 'Efforts', 'Inconvenience', 'Undesirable', 'Overwhelming',
                     'Cost', 'Updates', 'Risks'])

                for item in data:
                    writer.writerow(
                        [item.security_implementation_efforts_high, item.security_financial_enhancing_high,
                         item.security_efforts_practices_high,
                         item.security_inconvenience_outweighs_benefits, item.security_loss_functionality_undesirable,
                         item.security_incidence_response_overwhelming,
                         item.security_financial_cost_reasonable, item.security_updates_time_and_efforts_reasonable,
                         item.security_potential_risks_outweighs_implementations])

            data_frame = pd.read_csv('static/perceived_prevention_response_cost.csv')
            # Extract the features and target variables from the data
            y = data_frame['Risks']
            X = data_frame.drop('Risks', axis=1)

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train model
            """ Linear Regression """

            l_reg_model = LinearRegression()
            l_reg_model.fit(X_train, y_train)

            # train model to make prediction
            y_l_reg_train_pred = l_reg_model.predict(X_train)
            y_l_reg_test_pred = l_reg_model.predict(X_test)

            # Evaluate Model Performance
            l_reg_train_mse = mean_squared_error(y_train, y_l_reg_train_pred)
            l_reg_train_r2 = r2_score(y_train, y_l_reg_train_pred)
            l_reg_test_mse = mean_squared_error(y_test, y_l_reg_test_pred)
            l_reg_test_r2 = r2_score(y_test, y_l_reg_test_pred)

            """ Random Forest """

            # Training Model
            r_frt_model = RandomForestRegressor(max_depth=2, random_state=100)
            r_frt_model.fit(X_train, y_train)
            y_r_frt_train_pred = r_frt_model.predict(X_train)
            y_r_frt_test_pred = r_frt_model.predict(X_test)

            # Evaluate model performance
            r_frt_train_mse = mean_squared_error(y_train, y_r_frt_train_pred)
            r_frt_train_r2 = r2_score(y_train, y_r_frt_train_pred)
            r_frt_test_mse = mean_squared_error(y_test, y_r_frt_test_pred)
            r_frt_test_r2 = r2_score(y_test, y_r_frt_test_pred)

            # Get the input data from the form
            feature1 = float(request.POST.get('security_implementation_efforts_high'))
            feature2 = float(request.POST.get('security_financial_enhancing_high'))
            feature3 = float(request.POST.get('security_efforts_practices_high'))
            feature4 = float(request.POST.get('security_inconvenience_outweighs_benefits'))
            feature5 = float(request.POST.get('security_loss_functionality_undesirable'))
            feature6 = float(request.POST.get('security_incidence_response_overwhelming'))
            feature7 = float(request.POST.get('security_financial_cost_reasonable'))
            feature8 = float(request.POST.get('security_updates_time_and_efforts_reasonable'))
            # feature9 = float(request.POST.get('software_updates_security'))

            # Prepare the input data for prediction
            input_data = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8]]  # Create a list of lists if multiple samples

            # make predictions using linear regression
            y_l_reg_test_pred = l_reg_model.predict(input_data)

            # Make predictions using random forest
            y_r_frt_test_pred = r_frt_model.predict(input_data)

            # Evaluate model performance
            # r_frt_predict_mse = mean_squared_error(y_train, y_r_frt_test_pred)
            # r_frt_predict_r2 = r2_score(y_train, y_r_frt_test_pred)
            # r_frt_test_mse = mean_squared_error(y_test, ret)
            # r_frt_test_r2 = r2_score(y_test, ret)

            # Pass the predictions to the template for rendering
            context = {
                # linear regression train & test
                'l_reg_train_mse': l_reg_train_mse,
                'l_reg_train_r2': l_reg_train_r2,
                'l_reg_test_mse': l_reg_test_mse,
                'l_reg_test_r2': l_reg_test_r2,
                # linear regression predict
                'y_l_reg_test_pred': y_l_reg_test_pred,
                # random forest train & test
                'r_frt_train_mse': r_frt_train_mse,
                'r_frt_train_r2': r_frt_train_r2,
                'r_frt_test_mse': r_frt_test_mse,
                'r_frt_test_r2': r_frt_test_r2,
                # random forest predict
                'y_r_frt_test_pred': y_r_frt_test_pred
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
            warnings.filterwarnings("ignore")
            data = SocialNetworkSecurity.objects.all()
            file_path = os.path.join(settings.STATIC_ROOT, 'intended_user_behaviour.csv')

            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(
                    ['Maintenance', 'Proactive', 'Features', 'Personal', 'Updates', 'Security',
                     'Interacting', 'Block', 'Educate', 'Mindful'])

                for item in data:
                    writer.writerow(
                        [item.privacy_personal_info_maintenance, item.proactive_personal_info_access_management,
                         item.use_of_security_features,
                         item.personal_info_risk_consciousness, item.secure_account_with_regular_updates,
                         item.learn_social_network_security,
                         item.interacting_with_suspicious_accounts, item.block_report_suspicious_accounts,
                         item.educate_social_network_security, item.mind_privacy_policies_before_using])

            data_frame = pd.read_csv('static/intended_user_behaviour.csv')
            # Extract the features and target variables from the data
            y = data_frame['Mindful']
            X = data_frame.drop('Mindful', axis=1)

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train model
            """ Linear Regression """

            l_reg_model = LinearRegression()
            l_reg_model.fit(X_train, y_train)

            # train model to make prediction
            y_l_reg_train_pred = l_reg_model.predict(X_train)
            y_l_reg_test_pred = l_reg_model.predict(X_test)

            # Evaluate Model Performance
            l_reg_train_mse = mean_squared_error(y_train, y_l_reg_train_pred)
            l_reg_train_r2 = r2_score(y_train, y_l_reg_train_pred)
            l_reg_test_mse = mean_squared_error(y_test, y_l_reg_test_pred)
            l_reg_test_r2 = r2_score(y_test, y_l_reg_test_pred)

            """ Random Forest """

            # Training Model
            r_frt_model = RandomForestRegressor(max_depth=2, random_state=100)
            r_frt_model.fit(X_train, y_train)
            y_r_frt_train_pred = r_frt_model.predict(X_train)
            y_r_frt_test_pred = r_frt_model.predict(X_test)

            # Evaluate model performance
            r_frt_train_mse = mean_squared_error(y_train, y_r_frt_train_pred)
            r_frt_train_r2 = r2_score(y_train, y_r_frt_train_pred)
            r_frt_test_mse = mean_squared_error(y_test, y_r_frt_test_pred)
            r_frt_test_r2 = r2_score(y_test, y_r_frt_test_pred)

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
            # feature10 = float(request.POST.get('report_suspicious_activity'))

            # Prepare the input data for prediction
            input_data = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7,
                           feature8, feature9]]  # Create a list of lists if multiple samples

            # make predictions using linear regression
            y_l_reg_test_pred = l_reg_model.predict(input_data)

            # Make predictions using random forest
            y_r_frt_test_pred = r_frt_model.predict(input_data)

            # Evaluate model performance
            # r_frt_predict_mse = mean_squared_error(y_train, y_r_frt_test_pred)
            # r_frt_predict_r2 = r2_score(y_train, y_r_frt_test_pred)
            # r_frt_test_mse = mean_squared_error(y_test, ret)
            # r_frt_test_r2 = r2_score(y_test, ret)

            # Pass the predictions to the template for rendering
            context = {
                # linear regression train & test
                'l_reg_train_mse': l_reg_train_mse,
                'l_reg_train_r2': l_reg_train_r2,
                'l_reg_test_mse': l_reg_test_mse,
                'l_reg_test_r2': l_reg_test_r2,
                # linear regression predict
                'y_l_reg_test_pred': y_l_reg_test_pred,
                # random forest train & test
                'r_frt_train_mse': r_frt_train_mse,
                'r_frt_train_r2': r_frt_train_r2,
                'r_frt_test_mse': r_frt_test_mse,
                'r_frt_test_r2': r_frt_test_r2,
                # random forest predict
                'y_r_frt_test_pred': y_r_frt_test_pred
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
    form = DemographicInformationForm()
    if request.method == 'POST':
        form = DemographicInformationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Submitted Successfully.')
            warnings.filterwarnings("ignore")
            data = DemographicInformation.objects.all()

            file_path = os.path.join(settings.STATIC_ROOT, 'cybersecurity_data.csv')

            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(
                    ['Gender', 'Age', 'Academic Yr', 'Field', 'University', 'Funding', 'Mode', 'Knowledge', 'Usage',
                     'Active',
                     'Hours', 'Concern', 'Breaches', 'Measure', 'Sec Edu', 'Protection', 'Awareness', 'Settings',
                     'Sharing',
                     'Cyberbullying', 'Features', 'Sensitive', 'Encounters' 'Uprotect', 'TOS', 'Delete', 'SMedu'])

                for item in data:
                    writer.writerow([item.gender, item.age, item.academic_year, item.field_of_study, item.university,
                                     item.university_funding, item.mode_of_study, item.s_media_security_knowledge,
                                     item.social_media_usage, item.active_social_platforms,
                                     item.average_hours_s_media, item.s_media_security_concern,
                                     item.social_media_breaches,
                                     item.s_media_security_measure, item.privacy_security_education,
                                     item.s_media_self_protection,
                                     item.s_media_privacy_settings_awareness, item.often_review_privacy_settings,
                                     item.s_media_personal_info_sharing, item.victim_of_cyberbullying,
                                     item.s_media_privacy_security_features, item.s_media_sensitive_info_sharing,
                                     item.s_media_malicious_encounters, item.more_s_media_user_protection,
                                     item.s_media_privacy_policy_and_TOS, item.delete_account_due_to_privacy,
                                     item.s_media_security_education])

            # Read/Load the data (pandas)
            data_frame = pd.read_csv('static/cybersecurity_data.csv')

            # Extract the features and target variables from the data
            y = data_frame['SMedu']
            X = data_frame.drop('SMedu', axis=1)

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train model
            """ Linear Regression """

            l_reg_model = LinearRegression()
            l_reg_model.fit(X_train, y_train)

            # train model to make prediction
            y_l_reg_train_pred = l_reg_model.predict(X_train)
            y_l_reg_test_pred = l_reg_model.predict(X_test)

            # Evaluate Model Performance
            l_reg_train_mse = mean_squared_error(y_train, y_l_reg_train_pred)
            l_reg_train_r2 = r2_score(y_train, y_l_reg_train_pred)
            l_reg_test_mse = mean_squared_error(y_test, y_l_reg_test_pred)
            l_reg_test_r2 = r2_score(y_test, y_l_reg_test_pred)

            """ Random Forest """

            # Training Model
            r_frt_model = RandomForestRegressor(max_depth=2, random_state=100)
            r_frt_model.fit(X_train, y_train)
            y_r_frt_train_pred = r_frt_model.predict(X_train)
            y_r_frt_test_pred = r_frt_model.predict(X_test)

            # Evaluate model performance
            r_frt_train_mse = mean_squared_error(y_train, y_r_frt_train_pred)
            r_frt_train_r2 = r2_score(y_train, y_r_frt_train_pred)
            r_frt_test_mse = mean_squared_error(y_test, y_r_frt_test_pred)
            r_frt_test_r2 = r2_score(y_test, y_r_frt_test_pred)

            # Get the input data from the form
            feature1 = float(request.POST.get('gender'))
            feature2 = float(request.POST.get('age'))
            feature3 = float(request.POST.get('academic_year'))
            feature4 = float(request.POST.get('field_of_study'))
            feature5 = float(request.POST.get('university'))
            feature6 = float(request.POST.get('university_funding'))
            feature7 = float(request.POST.get('mode_of_study'))
            feature8 = float(request.POST.get('s_media_security_knowledge'))
            feature9 = float(request.POST.get('social_media_usage'))
            feature10 = float(request.POST.get('active_social_platforms'))
            feature11 = float(request.POST.get('average_hours_s_media'))
            feature12 = float(request.POST.get('s_media_security_concern'))
            feature13 = float(request.POST.get('social_media_breaches'))
            feature14 = float(request.POST.get('s_media_security_measure'))
            feature15 = float(request.POST.get('privacy_security_education'))
            feature16 = float(request.POST.get('s_media_self_protection'))
            feature17 = float(request.POST.get('s_media_privacy_settings_awareness'))
            feature18 = float(request.POST.get('often_review_privacy_settings'))
            feature19 = float(request.POST.get('s_media_personal_info_sharing'))
            feature20 = float(request.POST.get('victim_of_cyberbullying'))
            feature21 = float(request.POST.get('s_media_privacy_security_features'))
            feature22 = float(request.POST.get('s_media_sensitive_info_sharing'))
            feature23 = float(request.POST.get('s_media_malicious_encounters'))
            feature24 = float(request.POST.get('more_s_media_user_protection'))
            feature25 = float(request.POST.get('s_media_privacy_policy_and_TOS'))
            # feature26 = float(request.POST.get('delete_account_due_to_privacy'))

            # Prepare the input data for prediction
            input_data = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7,
                           feature8, feature9, feature10, feature11, feature12, feature13, feature14,
                           feature15, feature16, feature17, feature18, feature19, feature20, feature21,
                           feature22, feature23, feature24, feature25]]  # Create a list of lists if multiple samples

            # make predictions using linear regression
            y_l_reg_test_pred = l_reg_model.predict(input_data)

            # Make predictions using random forest
            y_r_frt_test_pred = r_frt_model.predict(input_data)

            # Evaluate model performance
            # r_frt_predict_mse = mean_squared_error(y_train, y_r_frt_test_pred)
            # r_frt_predict_r2 = r2_score(y_train, y_r_frt_test_pred)
            # r_frt_test_mse = mean_squared_error(y_test, ret)
            # r_frt_test_r2 = r2_score(y_test, ret)

            # Pass the predictions to the template for rendering
            context = {
                # linear regression train & test
                'l_reg_train_mse': l_reg_train_mse,
                'l_reg_train_r2': l_reg_train_r2,
                'l_reg_test_mse': l_reg_test_mse,
                'l_reg_test_r2': l_reg_test_r2,
                # linear regression predict
                'y_l_reg_test_pred': y_l_reg_test_pred,
                # random forest train & test
                'r_frt_train_mse': r_frt_train_mse,
                'r_frt_train_r2': r_frt_train_r2,
                'r_frt_test_mse': r_frt_test_mse,
                'r_frt_test_r2': r_frt_test_r2,
                # random forest predict
                'y_r_frt_test_pred': y_r_frt_test_pred
            }
            return render(request, 'results.html', context)
        else:
            messages.error(request, 'FAILED! Something went wrong.')
            context = {
                'form': form
            }
            return render(request, 'demographic_information.html', context)
    context = {
        'form': form
    }
    return render(request, 'demographic_information.html', context)


# view Results
def results(request):
    return render(request, 'results.html')


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
