import os
from django.contrib.auth.decorators import permission_required
from django.views.static import serve

@permission_required('juntagrico.can_view_exports')
def db_export(request):
  filepath = './chruutundruebli.db'
  return serve(request, os.path.basename(filepath), os.path.dirname(filepath))