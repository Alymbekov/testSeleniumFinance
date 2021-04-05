from django.urls import path

from . import views

urlpatterns = [
    path('v1/', views.FinanceDataList.as_view()),
    path('api/v1/parse/', views.ParseDataView.as_view()),
]
