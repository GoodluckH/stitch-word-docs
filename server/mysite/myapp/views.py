import os
from datetime import datetime

from django.shortcuts import render
from django.conf import settings
from django.http.response import HttpResponse
from rest_framework.views import APIView
from django.utils.encoding import smart_str

from .forms import DocumentForm
from .models import Document
from .managers import FilesProcessor

# State variable that indicates the file processing status
# "idle": not processing anything
# "processing": processing files
# "done": done processing files
STATE = {"status": "idle"}


# Views
def index(request):
    return render(request, 'myapp/index.html')


class Upload(APIView):
    """ Process Microsoft Word files received through POST requests
    """

    def post(self, request):
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            STATE['status'] = 'processing'
            for f in request.FILES.getlist('atw'):
                newfile = Document(docfile=f)
                newfile.save()
            
            output_filename = "OUT-ATW.docx"
            processor = FilesProcessor(output_filename)
            processor.process()
            STATE['status'] = 'done'
            return HttpResponse("Successfully processed files!")
        else:
            form = DocumentForm()
        return render(request, 'myapp/index.html')

def download(request):
    output_filename = "OUT-ATW.docx"
    file_path = os.path.join(settings.MEDIA_ROOT, output_filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            response['Content-Disposition'] = 'attachment; filename=' + output_filename
            response['X-Sendfile'] = smart_str(file_path)
            return response