from fastapi import FastAPI, UploadFile, File
from app.pdf_utils import save_pdf, load_and_split_pdf
from app.rag import create_vectorstore
from fastapi import Body
from app.rag import retrieve_chunks
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Chat with PDF API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],   # allow GET, POST, OPTIONS
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    # 1. Save PDF
    file_path = save_pdf(file)

    # 2. Load + split PDF
    chunks = load_and_split_pdf(file_path)

    # 3. Create FAISS vector DB
    create_vectorstore(chunks)

    return {
        "message": "PDF uploaded and indexed successfully",
        "chunks_indexed": len(chunks)
    }

@app.post("/ask")
async def ask_question(payload: dict = Body(...)):
    question = payload.get("question")

    if not question:
        return {"error": "Question is required"}

    docs = retrieve_chunks(question)

    # Build answer from retrieved chunks
    answer_text = "\n\n".join(
        doc.page_content for doc in docs
    )

    sources = []
    for doc in docs:
        sources.append({
            "page": doc.metadata.get("page", 0) + 1
        })

    return {
        "question": question,
        "answer": answer_text,
        "sources": sources
    }