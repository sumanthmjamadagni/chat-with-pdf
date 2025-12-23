from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from app.config import VECTORSTORE_DIR
import os

# VERY LIGHT MODEL (fits in 512MB)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-MiniLM-L3-v2"
)

def create_vectorstore(chunks):
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(VECTORSTORE_DIR)
    return db

def load_vectorstore():
    return FAISS.load_local(
        VECTORSTORE_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )

def retrieve_chunks(question: str, k: int = 3):
    db = load_vectorstore()
    return db.similarity_search(question, k=k)
