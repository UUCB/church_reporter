from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('report/<int:pk>', ReportDetailView.as_view(), name='report'),
    path('report/create', ReportCreateView.as_view(), name='report-create'),
    path('report/update/<int:pk>', ReportUpdateView.as_view(), name='report-update'),
    path('report/element/create', ReportElementCreateView.as_view(), name='report-element-create'),
    path('report/element/<int:pk>/update', ReportElementUpdateView.as_view(), name='report-element-update'),
    path('filter/create', ReportFilterCreateView.as_view(), name='filter-create'),
    path('filter/update/<int:pk>', ReportFilterUpdateView.as_view(), name='filter-update'),
    path('run_report', RunReportView.as_view(), name='run-report'),
]