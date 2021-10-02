import os
import mimetypes
import subprocess
from threading import Thread
from django.contrib.auth.decorators import permission_required
from django.http.response import HttpResponseRedirect, StreamingHttpResponse
from wsgiref.util import FileWrapper

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
  the_file = './db.json'
  filename = os.path.basename(the_file)
  chunk_size = 8192
  response = StreamingHttpResponse(FileWrapper(open(the_file, 'rb'), chunk_size),
                          content_type=mimetypes.guess_type(the_file)[0])
  response['Content-Length'] = os.path.getsize(the_file)    
  response['Content-Disposition'] = "attachment; filename=%s" % filename
  return response
