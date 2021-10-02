import os
from threading import Thread
from django.contrib.auth.decorators import permission_required
from django.core.management import call_command
from django.http.response import HttpResponseRedirect
from django.views.static import serve

def generate_db_export(filepath):
  with open(filepath, 'w') as f:
    call_command('dumpdata', stdout=f)


@permission_required('juntagrico.can_view_exports')
def db_export_generate(request):
  filepath = './db.json'
  Thread(target=generate_db_export, args=[filepath]).start()
  return HttpResponseRedirect('/my/export')

@permission_required('juntagrico.can_view_exports')
def db_export(request):
  filepath = './db.json'
  return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
