from openpyxl import Workbook

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

from juntagrico.entity.subs import Subscription
from juntagrico.entity.subtypes import SubscriptionType
from juntagrico.config import Config
from juntagrico.util.models import q_isactive
from django.utils import timezone
from django.utils.translation import gettext as _
from openpyxl.utils import get_column_letter


# API

def excel_export_subscriptions(request):
    filename = '{}_{}.xlsx'.format(str(Config.vocabulary('subscription_pl')), timezone.now().date())
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=' + filename
    wb = Workbook()

    # Sheet 1: Subscriptions with prices
    ws1 = wb.active
    ws1.title = str(Config.vocabulary('subscription_pl'))

    # header
    ws1.cell(1, 1, str(Config.vocabulary('member_pl')))
    ws1.column_dimensions['A'].width = 40
    ws1.cell(1, 2, str(_('E-Mail')))
    ws1.column_dimensions['B'].width = 30
    ws1.cell(1, 3, str(_('Gesamtpreis [{}]').format(Config.currency())))
    ws1.column_dimensions['C'].width = 17
    sub_types = SubscriptionType.objects.all()
    for column, subs_type in enumerate(sub_types, 4):
        ws1.cell(1, column, "EAT {}".format(subs_type.price))
        ws1.column_dimensions[get_column_letter(column)].width = 17

    # data
    for row, subscription in enumerate(Subscription.objects.filter(q_isactive()), 2):
        ws1.cell(row, 1, ", ".join([member.get_name() for member in subscription.current_members]))
        ws1.cell(row, 2, subscription.primary_member.email)
        ws1.cell(row, 3, subscription.price)
        for column, subs_type in enumerate(sub_types, 4):
            ws1.cell(row, column, subscription.parts.filter(type=subs_type).count())

    ws1.freeze_panes = ws1['A2']
    wb.save(response)
    return response


@permission_required('juntagrico.can_view_exports')
def export(request):
    return render(request, 'export.html', {})
