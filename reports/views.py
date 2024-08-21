from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, TemplateView
from django.shortcuts import render

from reports.forms import RunReportForm
from reports.models import Report, ReportElement, ReportFilter

import openpyxl

from pprint import pprint


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['reports'] = Report.objects.all()
        context['filters'] = ReportFilter.objects.all()
        return context


class ReportCreateView(CreateView):
    model = Report
    template_name = 'report_create.html'
    fields = ['title', 'description']


class ReportUpdateView(UpdateView):
    model = Report
    template_name = 'report_update.html'
    fields = ['title', 'description']


class ReportDeleteView(DeleteView):
    model = Report


class ReportDetailView(DetailView):
    model = Report
    context_object_name = 'report'
    template_name = 'report.html'

    def get_context_data(self, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        context['run_report_form'] = RunReportForm()
        return context


class ReportElementCreateView(CreateView):
    model = ReportElement
    fields = ['report', 'element_title', 'sheet_column', 'large', 'emphasized', 'order']
    template_name = 'report_element_create.html'


class ReportElementUpdateView(UpdateView):
    model = ReportElement
    fields = ['element_title', 'sheet_column', 'large', 'emphasized', 'order']
    template_name = 'report_element_update.html'


class ReportFilterCreateView(CreateView):
    model = ReportFilter
    fields = ['title', 'filter_column', 'filter_data']
    template_name = 'filter_create.html'


class ReportFilterUpdateView(UpdateView):
    model = ReportFilter
    fields = ['title', 'filter_column', 'filter_data']
    template_name = 'filter_update.html'


class RunReportView(FormView):
    template_name = 'report_output.html'
    form_class = RunReportForm

    def form_valid(self, form):
        print(form.cleaned_data['sheet_file'])
        context = {'report_data': []}
        report = form.cleaned_data['report']
        filter = form.cleaned_data['filter']
        workbook = openpyxl.load_workbook(form.cleaned_data['sheet_file'])
        sheet = workbook.active
        for row in sheet.rows:
            if filter:
                if row[openpyxl.utils.cell.column_index_from_string(filter.filter_column) - 1].value != filter.filter_data:
                    continue  # Skip rows that don't match the filter
            report_data_page = []
            for element in report.elements.all():
                report_data_page.append({
                    'title': element.element_title,
                    'data': row[openpyxl.utils.cell.column_index_from_string(element.sheet_column) - 1].value,
                    'element_obj': element,
                })
            context['report_data'].append(report_data_page)
        return render(self.request, self.template_name, context)

