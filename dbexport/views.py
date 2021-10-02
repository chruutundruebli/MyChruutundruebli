import os
from django.contrib.auth.decorators import permission_required
from django.core.management import call_command
from django.views.static import serve

@permission_required('juntagrico.can_view_exports')
def db_export(request):
  filepath = './db.json'
  with open(filepath, 'w') as f:
    call_command('dumpdata', stdout=f)
  return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
