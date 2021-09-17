import os
from docx import Document

dir = os.path.join(os.getcwd(), "docs")
files = os.listdir(dir)
def process(files):
        """Processes files initialized in self.files by merging them into one PDF file
        """
        if not files:
            return
        docs = []
        i = 0

        for file in files:
            docs.append(Document(os.path.join(dir, file)))   
            docs[i].add_page_break()
            if i != 0:
                for element in docs[i].element.body:
                    docs[0].element.body.append(element)
            i = i + 1

        docs[0].save(os.path.join(dir, "ATW.docx"))

if __name__ == "__main__":
    process(files)


