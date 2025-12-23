from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from app.config import VECTORSTORE_DIR
import os

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def create_vectorstore(chunks):
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(VECTORSTORE_DIR)
    return db

def load_vectorstore():
    if not os.path.exists(VECTORSTORE_DIR):
        raise RuntimeError("Vectorstore not found")

    return FAISS.load_local(
        VECTORSTORE_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )

def retrieve_chunks(question: str, k: int = 3):
    """
    Retrieve top-k relevant chunks for a question.
    """
    db = load_vectorstore()
    docs = db.similarity_search(question, k=k)
    return docs
