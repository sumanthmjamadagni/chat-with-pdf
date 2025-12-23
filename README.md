Chat with Your PDF – Retrieval Augmented Generation (RAG) System

1. Introduction
This project is a Chat with PDF application built using the concept of Retrieval-Augmented Generation (RAG).
It allows users to upload a PDF document and ask questions related to its content.
The system retrieves the most relevant parts of the document and provides context-aware answers along with source page numbers.

The main goal of this project is to demonstrate how Large Language Models can be combined with document retrieval systems to produce accurate and reliable answers.

2. Objective of the Project
The objectives of this project are:

To allow users to upload a PDF document
To store the PDF content in a vector database
To enable semantic question answering on the document
To return answers based only on the document content
To display source page numbers for transparency
To deploy the application on the cloud

3. What is Retrieval-Augmented Generation (RAG)?
Retrieval-Augmented Generation (RAG) is a technique that combines:

Information Retrieval – finding relevant document content using vector similarity
Answer Generation – forming answers using the retrieved context
Instead of directly generating answers from a language model’s memory, the model first retrieves relevant information from the uploaded PDF.
This approach:

Reduces hallucinations
Improves accuracy
Ensures answers are grounded in the document

4. System Architecture
Frontend (HTML, CSS, JavaScript) | | HTTP Requests v Backend (FastAPI) | v Vector Database (FAISS) | v Embedding Model (Sentence Transformers)

5. Technology Stack
Backend Technologies
Python – Core programming language
FastAPI – Backend REST API framework
LangChain – Used to manage RAG workflow
FAISS – Vector database for similarity search
Sentence Transformers – Local embedding model
PyPDF – PDF parsing and text extraction
Frontend Technologies
HTML – Structure of the UI
CSS – Styling and layout
JavaScript – API communication and interaction
Deployment & Tools
GitHub – Version control
Render – Backend deployment
Netlify – Frontend deployment


6. Backend Logic Explanation
6.1 PDF Upload
The user uploads a PDF file using the frontend
The backend validates the file type
The PDF is stored on the server
6.2 PDF Processing
The PDF is read page by page
Text is extracted from each page
Page numbers are stored as metadata
6.3 Text Chunking
The extracted text is split into small overlapping chunks
Chunking improves retrieval accuracy
Overlap ensures context continuity
6.4 Embeddings
Each chunk is converted into a numerical vector (embedding)
A Sentence Transformer model is used
This allows semantic comparison between questions and document text
6.5 Vector Database (FAISS)
All embeddings are stored in FAISS
FAISS performs fast similarity search
The vector database is saved locally for reuse
6.6 Question Answering
The user asks a question
The question is converted into an embedding
FAISS retrieves the most relevant chunks
The retrieved content is returned as the answer
Page numbers are included as source citations


7. Frontend Functionality
Upload PDF file
Enter question
View extracted answer
View source page numbers
Clean and user-friendly interface


8. Features Implemented
PDF upload and validation
Vector storage using FAISS
Semantic search
Context-aware answers
Source citation (page numbers)
Frontend-backend separation
Cloud-ready deployment


9. How to Run Locally
Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
Frontend

Open frontend/index.html in a browser



12. Deployment

Backend is deployed on Render

Frontend is deployed on Netlify

Public URLs are provided for access