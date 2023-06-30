from django.shortcuts import render, redirect
from .models import DemographicInformation
from .forms import DemographicInformationForm
from django.contrib import messages
from django.http import HttpResponse, Http404
import csv
from django.conf import settings
import os

""" ml model """
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import numpy as np
import warnings


# SECTION A.
def demographic_information(request):
    form = DemographicInformationForm()
    if request.method == 'POST':
        form = DemographicInformationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Submitted Successfully.')
            return redirect('/')
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
                             item.s_media_security_measure, item.privacy_security_education, item.s_media_self_protection,
                             item.s_media_privacy_settings_awareness, item.often_review_privacy_settings,
                             item.s_media_personal_info_sharing, item.victim_of_cyberbullying,
                             item.s_media_privacy_security_features, item.s_media_sensitive_info_sharing,
                             item.s_media_malicious_encounters, item.more_s_media_user_protection,
                             item.s_media_privacy_policy_and_TOS, item.delete_account_due_to_privacy,
                             item.s_media_security_education])

        # data_fields = data.values_list('gender', 'age', 'academic_year', 'field_of_study', 'university',
        #                                'university_funding', 'mode_of_study', 's_media_security_knowledge',
        #                                'social_media_usage', 'active_social_platforms', 'average_hours_s_media',
        #                                's_media_security_concern', 'social_media_breaches', 's_media_security_measure',
        #                                'privacy_security_education', 's_media_self_protection',
        #                                's_media_privacy_settings_awareness', 'often_review_privacy_settings',
        #                                's_media_personal_info_sharing', 'victim_of_cyberbullying',
        #                                's_media_privacy_security_features', 's_media_sensitive_info_sharing',
        #                                's_media_malicious_encounters', 'more_s_media_user_protection',
        #                                's_media_privacy_policy_and_TOS', 'delete_account_due_to_privacy',
        #                                's_media_security_education')
        # for item in data_fields:
        #     writer.writerow(item)

    # Read/Load the data (pandas)
    data_frame = pd.read_csv('static/cybersecurity_data.csv')

    y = data_frame['PMT']
    x = data_frame.drop('PMT', axis=1)

    # split data sets
    x_test, x_train, y_test, y_train = train_test_split(x, y, test_size=0.2, random_state=100)

    """ Linear Regression """
    # build model
    l_reg = LinearRegression()
    l_reg.fit(x_train, y_train)

    # train model to make prediction
    y_l_reg_train_pred = l_reg.predict(x_train)
    y_l_reg_test_pred = l_reg.predict(x_test)

    # Evaluate Model Performance
    l_reg_train_mse = mean_squared_error(y_train, y_l_reg_train_pred)
    l_reg_train_r2 = r2_score(y_train, y_l_reg_train_pred)
    l_reg_test_mse = mean_squared_error(y_test, y_l_reg_test_pred)
    l_reg_test_r2 = r2_score(y_test, y_l_reg_test_pred)
    #
    # create table
    l_reg_results = pd.DataFrame(['Linear Regression', l_reg_train_mse, l_reg_train_r2, l_reg_test_mse, l_reg_test_r2]).transpose()
    l_reg_results.columns = ['METHOD', 'Training MSE', 'Training R2', 'Testing MSE', 'Training R2']
    # print(lr_results)
    #
    """ Random Forest """

    # Training Model
    r_frt = RandomForestRegressor(max_depth=2, random_state=100)
    r_frt.fit(x_train, y_train)
    y_r_frt_train_pred = r_frt.predict(x_train)
    y_r_frt_test_pred = r_frt.predict(x_test)
    #
    # Evaluate model performance
    r_frt_train_mse = mean_squared_error(y_train, y_r_frt_train_pred)
    r_frt_train_r2 = r2_score(y_train, y_r_frt_train_pred)
    r_frt_test_mse = mean_squared_error(y_test, y_r_frt_test_pred)
    r_frt_test_r2 = r2_score(y_test, y_r_frt_test_pred)
    #
    # create table
    r_frt_results = pd.DataFrame(['RandomForest', r_frt_train_mse, r_frt_train_r2, r_frt_test_mse, r_frt_test_r2]).transpose()
    r_frt_results.columns = ['METHOD', 'Training MSE', 'Training R2', 'Testing MSE', 'Training R2']
    # # print(rf_results)
    #
    # model comparison
    data_frame_models = pd.concat([l_reg_results, r_frt_results], axis=0).reset_index(drop=True)
    # print(data_frame_models)
    #
    # # data visualization of prediction results
    # plt.figure(figsize=(5, 5))
    # plt.scatter(x=y_train, y=y_l_reg_train_pred, alpha=0.3)
    # z = np.polyfit(y_train, y_l_reg_train_pred, 1)
    # p = np.poly1d(z)
    # plt.plot(y_train, p(y_train), '#F8766D')
    # plt.ylabel('Prediction')
    # plt.xlabel('Experimental')
    # plt.show()

    # """ replace values of target to 1 & 0 to train model """
    # data_frame['PMT'].replace(['THREAT APPRAISAL', 'COPING APPRAISAL'], [1, 0], inplace=True)
    # data_frame['GENDER'].replace(['MALE', 'FEMALE'], [1, 0], inplace=True)
    # data_frame['EDUCATION'].replace(['A', 'B', 'C', 'D', 'E'], [0.2, 0.4, 0.6, 0.8, 1.0], inplace=True)
    #
    # """ build the model """
    # # split data to x & y
    # x = data_frame[['AGE', 'GENDER', 'EDUCATION']]  # top 3 features
    # y = data_frame[['PMT']]  # target output
    #
    # # split dataset into train and test
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)
    #
    # # create a logistic regression body
    # logreg = LogisticRegression()
    # logreg.fit(x_train, y_train)
    #
    # # predict likelihood of tested outcome using logistic regression body
    # y_pred = logreg.predict(x_test)
    # print(x_test)  # test dataset
    # print(y_pred)  # predicted values
    #
    # """ Evaluate Model Performance (predictive analysis) """
    #
    # # call these scores by inserting these lines of code
    # print('Accuracy: ', metrics.accuracy_score(y_test, y_pred))
    # print('Recall: ', metrics.recall_score(y_test, y_pred, zero_division=1))
    # print('Precision: ', metrics.precision_score(y_test, y_pred, zero_division=1))
    # print('CL Report: ', metrics.classification_report(y_test, y_pred, zero_division=1))
    #
    # # regression itself
    # res = sm.OLS(y, x).fit()
    # disp = res.summary()
    # print(disp)
    #
    # """ Receiver Operating Characteristic - ROC Curve """
    # # define metrics
    # y_pred_proba = logreg.predict_proba(x_test)[::, 1]
    #
    # # calculate true positive & false positive rates
    # false_positive_rate, true_positive_rate, _ = metrics.roc_curve(y_test, y_pred_proba)
    #
    # # calculate the AUC to see the model's performance
    # auc = metrics.roc_auc_score(y_test, y_pred_proba)
    #
    # # plot ROC curve
    # plt.plot(false_positive_rate, true_positive_rate, label='AUC= ' + str(auc))
    # plt.title('ROC Curve')
    # plt.xlabel('True Positive Rate')
    # plt.ylabel('False Positive Rate')
    # plt.legend(loc=4)
    # plt.show()
    #
    context = {
        # 'data': data,
        'data_frame': data_frame,
        'x_train': x_train,
        'x_test': x_test,
        'l_reg_results': l_reg_results,
        'r_frt_results': r_frt_results,
        'data_frame_models ': data_frame_models,
        'plt': plt

        # 'df': df
    }
    return render(request, 'results.html', context)
