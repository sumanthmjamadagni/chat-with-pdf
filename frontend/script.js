const BACKEND_URL = "https://backend-chat-pdf.onrender.com/";

async function uploadPDF() {
    const fileInput = document.getElementById("pdfFile");
    const status = document.getElementById("uploadStatus");

    if (!fileInput.files.length) {
        alert("Please select a PDF");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    status.innerText = "Uploading...";

    const res = await fetch(`${BACKEND_URL}/upload-pdf`, {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    status.innerText = data.message;
}

async function askQuestion() {
    const question = document.getElementById("question").value;
    const answerBox = document.getElementById("answer");
    const sourceBox = document.getElementById("sources");

    if (!question) {
        alert("Enter a question");
        return;
    }

    answerBox.innerText = "Thinking...";
    sourceBox.innerText = "";

    const res = await fetch(`${BACKEND_URL}/ask`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question })
    });

    const data = await res.json();

    answerBox.innerText = data.answer;

    const pages = data.sources.map(s => s.page).join(", ");
    sourceBox.innerText = "Source pages: " + pages;
}
