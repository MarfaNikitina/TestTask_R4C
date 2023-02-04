from datetime import datetime, timedelta

import openpyxl
from django.db.models import Q, Count, QuerySet
from openpyxl import Workbook

from robots.models import Robot

CURRENT_DATE = datetime.now()
WEEK_AGO_DATE = CURRENT_DATE - timedelta(days=7)


def _get_production_for_report() -> list[QuerySet]:
    models_list = Robot.objects.all().values_list('model', flat=True).distinct()
    production = []
    for model in models_list:
        unique_model = Robot.objects.filter(model=model)
        model_production = unique_model.filter(
            Q(created__gte=WEEK_AGO_DATE) & Q(created__lte=CURRENT_DATE)). \
            values('model', 'version'). \
            annotate(count_by_week=Count('serial'))
        production.append(model_production)
    return production


def make_report_workbook() -> Workbook:
    """Function that makes report about robot production for last week."""
    production = _get_production_for_report()
    report_data = openpyxl.Workbook()
    for index, note in enumerate(production):
        sheet = report_data.create_sheet(f'Страница{index + 1}', index)
        sheet['A1'] = 'Модель'
        sheet['B1'] = 'Версия'
        sheet['C1'] = 'Количество за неделю'
        row = 2
        for robot in note:
            sheet[row][0].value = robot['model']
            sheet[row][1].value = robot['version']
            sheet[row][2].value = robot['count_by_week']
            row += 1
    return report_data
