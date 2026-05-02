import streamlit as st

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from PyPDF2 import PdfReader
import google.generativeai as genai
import os
from dotenv import load_dotenv


def load_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


embed_model = SentenceTransformer("all-MiniLM-L6-v2")
def embed_chunks(chunks):
    return embed_model.encode(chunks)


def create_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index


def retrieve(query, k, index, chunks):
    query_vec = embed_model.encode([query])
    distances, indices = index.search(query_vec, k)

    results = [chunks[i] for i in indices[0]]
    return results

load_dotenv()
key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=key)

llm = genai.GenerativeModel("gemini-flash-latest")


def ask_gemini(context, query):
    prompt = f"""
    Answer ONLY using the context below.
    If the answer is not present, say "Not found in document".

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.generate_content(prompt)
    return response.text

def rag_pipeline(query, index, chunks):
    retrieved_chunks = retrieve(query, 3, index, chunks)
    context = " ".join(retrieved_chunks)

    answer = ask_gemini(context, query)
    return answer

# Streamlit part
st.title("📄 PDF Chatbot (RAG)")

uploaded_file = st.file_uploader("Upload PDF")

if uploaded_file:
    text = load_pdf(uploaded_file)
    chunks = chunk_text(text)
    embeddings = embed_chunks(chunks)
    index = create_faiss_index(embeddings)

    query = st.text_input("Ask a question")

    if query:
        answer = rag_pipeline(query, index, chunks)
        st.write(answer)