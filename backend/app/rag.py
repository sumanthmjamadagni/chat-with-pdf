from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.config import VECTORSTORE_DIR
import os

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

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

def retrieve_chunks(question, k=3):
    db = load_vectorstore()
    return db.similarity_search(question, k=k)
