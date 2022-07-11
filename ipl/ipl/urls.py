"""ipl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from iplapp.views import matches_played_per_year,number_of_matches_won_per_team,extra_runs_conceded

urlpatterns = [
    path('',matches_played_per_year),
    path('problem2/',number_of_matches_won_per_team),
    path('problem3/',extra_runs_conceded),
    path('admin/', admin.site.urls),
]
