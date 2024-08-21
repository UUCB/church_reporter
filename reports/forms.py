from django import forms
from .models import Report, ReportFilter


class RunReportForm(forms.Form):
    report = forms.ModelChoiceField(queryset=Report.objects.all())
    filter = forms.ModelChoiceField(queryset=ReportFilter.objects.all())
    sheet_file = forms.FileField()
