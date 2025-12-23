import os
from pypdf import PdfReader
from app.config import UPLOAD_DIR
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def save_pdf(file):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return file_path

def load_and_split_pdf(file_path):
    reader = PdfReader(file_path)
    documents = []

    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            documents.append(
                Document(
                    page_content=text,
                    metadata={"page": page_num + 1}
                )
            )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_documents(documents)
