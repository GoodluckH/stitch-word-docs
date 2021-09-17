from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.views import APIView

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
            processor = FilesProcessor()
            processor.process()
            STATE['status'] = 'done'
            return HttpResponse("Successfully processed files!")
        else:
            form = DocumentForm()
        return render(request, 'myapp/index.html')
