import os

from docx import Document
from pathlib import Path

class FilesProcessor:
    """Tools needed to process Microsoft Word files

    Attributes
        files: An array of files to be processed.
    To use:
    >>> processor = FilesProcessor(model)
    >>> processor.process()
    """

    def __init__(self, model):
        """Inits FilesProcessor with files"""
        self.BASE_DIR = Path(__file__).resolve().parent
        self.model = model
        self.files = os.listdir(os.path.join(self.BASE_DIR, "docs"))
    
    def process(self):
        """Processes files initialized in self.files by merging them into one PDF file
        """
        if not self.files:
            return
        docs = []
        i = 0
        for file in self.files:
            docs.append(Document(file))
            if (i != 0):
                docs[i].add_page_break()
                for element in docs[i].element.body:
                    docs[0].element.body.append(element)
            i = i + 1

        docs[0].save(os.path.join(self.BASE_DIR, "docs"))

