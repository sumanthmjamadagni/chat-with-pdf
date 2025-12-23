import os

# Base directory of backend
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Upload and vectorstore directories
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
VECTORSTORE_DIR = os.path.join(BASE_DIR, "vectorstore")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(VECTORSTORE_DIR, exist_ok=True)

# Optional OpenAI API key (not required for this deployment)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
