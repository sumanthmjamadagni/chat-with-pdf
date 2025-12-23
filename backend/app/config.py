import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

print("DEBUG: OPENAI_API_KEY loaded:", bool(OPENAI_API_KEY))

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY not set")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
VECTORSTORE_DIR = os.path.join(BASE_DIR, "vectorstore")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(VECTORSTORE_DIR, exist_ok=True)
