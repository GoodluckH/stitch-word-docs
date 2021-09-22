import os

from docx import Document
from datetime import datetime
from pathlib import Path

class FilesProcessor:
    """Tools needed to process Microsoft Word files

    Attributes
        files: An array of files to be processed.
        output_filename: A string that describes the merged file's filename with extension '.docx'
    To use:
    >>> processor = FilesProcessor("filename")
    >>> processor.process()
    """

    def __init__(self, output_filename):
        """Inits FilesProcessor with files"""
        self.BASE_DIR = Path(__file__).resolve().parent
        self.files = os.listdir(os.path.join(self.BASE_DIR, "docs"))
        self.output_filename = output_filename

    def process(self):
        """Processes files initialized in self.files by merging them into one PDF file
        """
        if not self.files:
            return
        docs = []
        for file in self.files:
            if file == self.output_filename:
                os.remove(os.path.join(self.BASE_DIR, "docs", file))

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

        docs[0].save(os.path.join(self.BASE_DIR, "docs", self.output_filename))

        for file in self.files:
            if file != self.output_filename:
                os.remove(os.path.join(self.BASE_DIR, "docs", file))
