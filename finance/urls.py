from django.urls import path

from . import views

urlpatterns = [
    path('', views.FinanceDataList.as_view()),
    path('parse/', views.ParseDataView.as_view()),
]
