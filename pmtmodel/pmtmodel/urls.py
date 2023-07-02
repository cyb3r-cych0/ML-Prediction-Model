"""
URL configuration for pmtmodel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pmtapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('demographic_information/', views.demographic_information, name='demographic_information'),
    path('perceived_severity/', views.perceived_severity, name='perceived_severity'),
    path('perceived_vulnerability/', views.perceived_vulnerability, name='perceived_vulnerability'),
    path('perceived_response_efficacy/', views.perceived_response_efficacy, name='perceived_response_efficacy'),
    path('perceived_self_efficacy/', views.perceived_self_efficacy, name='perceived_self_efficacy'),
    path('perceived_prevention_response_cost/', views.perceived_prevention_response_cost, name='perceived_prevention_response_cost'),
    path('intended_user_behaviour/', views.intended_user_behaviour, name='intended_user_behaviour'),
    path('results/', views.results, name='results')
]
