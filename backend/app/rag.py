from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os
from app.config import VECTORSTORE_DIR

VEC_PATH = os.path.join(VECTORSTORE_DIR, "tfidf.pkl")

def create_vectorstore(chunks):
    texts = [c.page_content for c in chunks]

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(texts)

    with open(VEC_PATH, "wb") as f:
        pickle.dump((vectorizer, vectors, chunks), f)

def retrieve_chunks(question, k=3):
    with open(VEC_PATH, "rb") as f:
        vectorizer, vectors, chunks = pickle.load(f)

    q_vec = vectorizer.transform([question])
    scores = cosine_similarity(q_vec, vectors)[0]

    top_k = scores.argsort()[-k:][::-1]
    return [chunks[i] for i in top_k]
