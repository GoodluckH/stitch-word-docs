import os

from docx import Document
from pathlib import Path


class FilesProcessor:
    """Tools needed to process Microsoft Word files

    Attributes
        files: An array of files to be processed.
    To use:
    >>> processor = FilesProcessor()
    >>> processor.process()
    """

    def __init__(self):
        """Inits FilesProcessor with files"""
        self.BASE_DIR = Path(__file__).resolve().parent
        self.files = os.listdir(os.path.join(self.BASE_DIR, "docs"))

    def process(self):
        """Processes files initialized in self.files by merging them into one PDF file
        """
        if not self.files:
            return
        docs = []
        i = 0
        for file in self.files:
            if file == ".DS_Store":
                continue
            docs.append(Document(os.path.join(self.BASE_DIR, "docs", file)))
            docs[i].add_page_break()
            if (i != 0):
                for element in docs[i].element.body:
                    docs[0].element.body.append(element)
            i = i + 1

        docs[0].save(os.path.join(self.BASE_DIR, "docs", "ATW.docx"))
