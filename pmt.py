import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import statsmodels.api as sm

""" feature selection"""
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

""" classification report """
from sklearn import metrics

from sklearn.linear_model import SGDClassifier

import warnings

warnings.filterwarnings("ignore")

# Read/Load the data (pandas)
data_frame = pd.read_csv('cybersecurity_data_features_1.csv')

""" replace values of target to 1 & 0 to train model """
data_frame['PMT'].replace(['THREAT APPRAISAL', 'COPING APPRAISAL'], [1, 0], inplace=True)
data_frame['GENDER'].replace(['MALE', 'FEMALE'], [1, 0], inplace=True)
data_frame['EDUCATION'].replace(['A', 'B', 'C', 'D', 'E'], [0.2, 0.4, 0.6, 0.8, 1.0], inplace=True)


""" build the model """
# split data to x & y
x = data_frame[['AGE', 'GENDER', 'EDUCATION']]  # top 3 features
y = data_frame[['PMT']]  # target output

# split dataset into train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=100)

# create a logistic regression body
logreg = LogisticRegression()
logreg.fit(x_train, y_train)

# predict likelihood of tested outcome using logistic regression body
y_pred = logreg.predict(x_test)
print(x_test)  # test dataset
print(y_pred)  # predicted values

""" Evaluate Model Performance (predictive analysis) """

# call these scores by inserting these lines of code
print('Accuracy: ', metrics.accuracy_score(y_test, y_pred))
print('Recall: ', metrics.recall_score(y_test, y_pred, zero_division=1))
print('Precision: ', metrics.precision_score(y_test, y_pred, zero_division=1))
print('CL Report: ', metrics.classification_report(y_test, y_pred, zero_division=1))

# regression itself
results = sm.OLS(y, x).fit()
disp = results.summary()
print(disp)

""" Receiver Operating Characteristic - ROC Curve """
# define metrics
y_pred_proba = logreg.predict_proba(x_test)[::, 1]

# calculate true positive & false positive rates
false_positive_rate, true_positive_rate, _ = metrics.roc_curve(y_test, y_pred_proba)

# calculate the AUC to see the model's performance
auc = metrics.roc_auc_score(y_test, y_pred_proba)

# plot ROC curve
plt.plot(false_positive_rate, true_positive_rate, label='AUC= ' + str(auc))
plt.title('ROC Curve')
plt.xlabel('True Positive Rate')
plt.ylabel('False Positive Rate')
plt.legend(loc=4)
plt.show()
