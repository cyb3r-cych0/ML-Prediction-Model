from django.shortcuts import render, redirect

from .models import DemographicInformation, PerceivedSeverity, PerceivedVulnerability, PerceivedResponseEfficacy, \
    PerceivedSelfEfficacy
from .forms import DemographicInformationForm, PerceivedSeverityForm, PerceivedVulnerabilityForm, \
    PerceivedResponseEfficacyForm, PerceivedSelfEfficacyForm
from django.contrib import messages
from django.http import HttpResponse, Http404
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
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import numpy as np
import warnings


def home(request):
    return render(request, 'home.html')


def perceived_severity(request):
    return render(request, 'perceived_severity.html')


def perceived_vulnerability(request):
    return render(request, 'perceived_vulnerability.html')


def perceived_response_efficacy(request):
    return render(request, 'perceived_response_efficacy.html')


def perceived_self_efficacy(request):
    return render(request, 'perceived_self_efficacy.html')


def perceived_prevention_response_cost(request):
    return render(request, 'perceived_prevention_response_cost.html')


def intended_user_behaviour(request):
    return render(request, 'intended_user_behaviour.html')


# SECTION A.
def demographic_information(request):
    form = DemographicInformationForm()
    if request.method == 'POST':
        form = DemographicInformationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Submitted Successfully.')
            return redirect('/demographic_information')
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
    warnings.filterwarnings("ignore")
    data = DemographicInformation.objects.all()

    file_path = os.path.join(settings.STATIC_ROOT, 'cybersecurity_data.csv')

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ['Gender', 'Age', 'Academic Yr', 'Field', 'University', 'Funding', 'Mode', 'Knowledge', 'Usage', 'Active',
             'Hours', 'Concern', 'Breaches', 'Measure', 'Sec Edu', 'Protection', 'Awareness', 'Settings', 'Sharing',
             'Cyberbullying', 'Features', 'Sensitive', 'Encounters' 'Uprotect', 'TOS', 'Delete', 'SMedu', 'PMT'])

        for item in data:
            writer.writerow([item.gender, item.age, item.academic_year, item.field_of_study, item.university,
                             item.university_funding, item.mode_of_study, item.s_media_security_knowledge,
                             item.social_media_usage, item.active_social_platforms,
                             item.average_hours_s_media, item.s_media_security_concern, item.social_media_breaches,
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

    Y = data_frame['Delete']
    X = data_frame.drop('Delete', axis=1)

    # split data sets
    X_test, X_train, Y_test, Y_train = train_test_split(X, Y, test_size=0.2, random_state=100)

    """ Linear Regression """
    # build model
    l_reg = LinearRegression()
    l_reg.fit(X_train, Y_train)

    # train model to make prediction
    y_l_reg_train_pred = l_reg.predict(X_train)
    y_l_reg_test_pred = l_reg.predict(X_test)

    # Evaluate Model Performance
    l_reg_train_mse = mean_squared_error(Y_train, y_l_reg_train_pred)
    l_reg_train_r2 = r2_score(Y_train, y_l_reg_train_pred)
    l_reg_test_mse = mean_squared_error(Y_test, y_l_reg_test_pred)
    l_reg_test_r2 = r2_score(Y_test, y_l_reg_test_pred)

    """ Random Forest """

    # Training Model
    r_frt = RandomForestRegressor(max_depth=2, random_state=100)
    r_frt.fit(X_train, Y_train)
    y_r_frt_train_pred = r_frt.predict(X_train)
    y_r_frt_test_pred = r_frt.predict(X_test)
    #
    # Evaluate model performance
    r_frt_train_mse = mean_squared_error(Y_train, y_r_frt_train_pred)
    r_frt_train_r2 = r2_score(Y_train, y_r_frt_train_pred)
    r_frt_test_mse = mean_squared_error(Y_test, y_r_frt_test_pred)
    r_frt_test_r2 = r2_score(Y_test, y_r_frt_test_pred)

    # """ replace values of target to 1 & 0 to train model """
    # data_frame['PMT'].replace(['THREAT APPRAISAL', 'COPING APPRAISAL'], [1, 0], inplace=True)
    # data_frame['GENDER'].replace(['MALE', 'FEMALE'], [1, 0], inplace=True)
    # data_frame['EDUCATION'].replace(['A', 'B', 'C', 'D', 'E'], [0.2, 0.4, 0.6, 0.8, 1.0], inplace=True)

    """ build the model """
    # split data to x & y
    x = data_frame[['Age', 'Gender', 'Academic Yr']]  # top 3 features
    y = data_frame[['PMT']]  # target output

    # split dataset into train and test
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)

    # create a logistic regression body
    logreg = LogisticRegression()
    logreg.fit(x_train, y_train)

    # predict likelihood of tested outcome using logistic regression body
    y_pred = logreg.predict(x_test)
    # print(x_test)  # test dataset
    # print(y_pred)  # predicted values

    """ Evaluate Model Performance (predictive analysis) """
    accuracy = metrics.accuracy_score(y_test, y_pred)
    recall = metrics.recall_score(y_test, y_pred, zero_division=1)
    precision = metrics.precision_score(y_test, y_pred, zero_division=1)
    report = metrics.classification_report(y_test, y_pred, zero_division=1)

    # regression itself
    res = sm.OLS(y, x).fit()
    disp = res.summary()
    # print(disp)

    """ Receiver Operating Characteristic - ROC Curve """
    # # define metrics
    # y_pred_proba = logreg.predict_proba(x_test)[::, 1]
    #
    # # calculate true positive & false positive rates
    # false_positive_rate, true_positive_rate, _ = metrics.roc_curve(y_test, y_pred_proba)
    #
    # # calculate the AUC to see the model's performance
    # auc = metrics.roc_auc_score(y_test, y_pred_proba)

    # # plot ROC curve
    # plt.plot(false_positive_rate, true_positive_rate, label='AUC= ' + str(auc))
    # plt.title('ROC Curve')
    # plt.xlabel('True Positive Rate')
    # plt.ylabel('False Positive Rate')
    # plt.legend(loc=4)
    # plts = plt.show()

    context = {
        # 'data': data,
        'data_frame': data_frame,
        'x_test': x_test,
        'y_pred': y_pred,
        'accuracy': accuracy,
        'recall': recall,
        'precision ': precision,
        'report': report,
        'disp': disp,
        # 'plts': plts
        'X_train': X_train,
        'Y_test': Y_test,
        'r_frt_train_mse': r_frt_train_mse,
        'r_frt_train_r2': r_frt_train_r2,
        'r_frt_test_mse': r_frt_test_mse,
        'r_frt_test_r2': r_frt_test_r2,
        'l_reg_train_mse': l_reg_train_mse,
        'l_reg_train_r2': l_reg_train_r2,
        'l_reg_test_mse': l_reg_test_mse,
        'l_reg_test_r2': l_reg_test_r2
    }
    return render(request, 'results.html', context)
