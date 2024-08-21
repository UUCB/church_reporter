from django.db import models
from django.urls import reverse


class Report(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def next_element_order(self):
        return max([0, ] + [element.order for element in self.elements.all()]) + 10

    def get_absolute_url(self):
        return reverse('report', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class ReportElement(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='elements')
    element_title = models.CharField(max_length=255, null=True, blank=True)
    sheet_column = models.CharField(max_length=3)
    large = models.BooleanField(default=False)
    emphasized = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return f'"{self.element_title}" from column {self.sheet_column}'

    def get_absolute_url(self):
        return reverse('report', kwargs={'pk': self.report.pk})


class ReportFilter(models.Model):
    title = models.CharField(max_length=255)
    filter_column = models.CharField(max_length=3, help_text='Filter based on this column\'s data.')
    filter_data = models.CharField(
        max_length=255,
        help_text='Rows where the above column contains this data will be used in the report.'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')
