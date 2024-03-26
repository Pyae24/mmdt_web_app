from django.urls import path
from . import views
app_name = "survey"
urlpatterns = [
    path("", views.SurveyPage.index, name='index'),
    path("survey/<int:survey_id>/", views.SurveyPage.survey_detail, name='survey_detail'),
    path("all_results/", views.SurveyPage.all_results, name='all_results')
]
