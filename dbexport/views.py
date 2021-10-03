import os
import subprocess
from threading import Thread
from django.contrib.auth.decorators import permission_required
from django.http.response import HttpResponseRedirect
from django.views.static import serve

def generate_db_export():
  process = subprocess.Popen(['./manage.py', 'dumpdata', '-o', 'db.json'],
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE)
  stdout, stderr = process.communicate()
  stdout, stderr

@permission_required('juntagrico.can_view_exports')
def db_export_generate(request):
  Thread(target=generate_db_export).start()
  return HttpResponseRedirect('/my/export')

@permission_required('juntagrico.can_view_exports')
def db_export(request):
  filepath = './db.json'
  return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
