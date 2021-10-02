from django.contrib.auth.decorators import permission_required
from django.http.response import JsonResponse

from chruutundruebli.settings import DATABASES

@permission_required('juntagrico.can_view_exports')
def db_export(request):
  
  return JsonResponse(DATABASES)
