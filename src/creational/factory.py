from abc import ABC


class Document(ABC):
    def create(self) -> str:
        raise NotImplementedError

class WordDocument(Document):
    def create(self):
        return "Word Document Created"

class PdfDocument(Document):
    def create(self):
        return "PDF Document Created"

class DocumentFactory:
    @staticmethod
    def get_document(doc_type):
        if doc_type == "word":
            return WordDocument()
        elif doc_type == "pdf":
            return PdfDocument()
        else:
            return WordDocument()

def execute():
    doc = DocumentFactory.get_document("word")
    print(doc.create())
