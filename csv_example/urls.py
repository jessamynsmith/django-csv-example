from django.urls import path

from csv_example import views


urlpatterns = [
    path('', views.download_csv, name='download_csv'),
]
