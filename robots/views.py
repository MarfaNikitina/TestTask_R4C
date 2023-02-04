import datetime

from django.core.files.temp import NamedTemporaryFile
from django.http import HttpResponse
from rest_framework.decorators import api_view

from robots.services import make_report_workbook


@api_view()
def download_report(request):
    """Function that downloads report for director."""
    with NamedTemporaryFile() as file_:
        report_workbook = make_report_workbook()
        report_workbook.save(file_.name)
        response = HttpResponse(file_, content_type='xlsx')
        response_file_name = f'report-{datetime.datetime.now()}.xlsx'
        response['Content-Disposition'] = f'attachment; filename={response_file_name}'
        return response
