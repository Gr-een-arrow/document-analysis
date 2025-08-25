# 📄 Document Analysis RAG System  

A **document analysis assistant** powered by **Retrieval-Augmented Generation (RAG)**.  
This system allows users to **upload documents**, **ask queries**, and receive **AI-generated answers with citations** from the original text.  

---

## 🚀 Features  
- 📂 **Multi-format Document Upload**: PDF, DOCX, TXT, Excel  
- 🔍 **Semantic Search**: Retrieve relevant chunks using embeddings + FAISS  
- 🤖 **RAG Question Answering**: LLM generates answers based on document context  
- 📑 **Citations & Highlighting**: See *exact source text* used for answers  
- 💬 **Conversational Queries**: Ask follow-up questions with memory  

---


## 🛠️ Tech Stack  

**Backend**  
- [Python 3.10+](https://www.python.org/)  
- [Django](https://www.djangoproject.com/) – API framework  
- [LangChain](https://www.langchain.com/) – RAG pipeline  
- [Sentence-Transformers](https://www.sbert.net/) – embeddings  
- [FAISS](https://faiss.ai/) – vector database  

**LLM Inference**  
- [Ollama](https://ollama.ai/) or [vLLM](https://github.com/vllm-project/vllm) – for running open-source LLMs (e.g., Llama 3, Mistral)  


**Frontend**  
- [Next.js](https://nextjs.org/) + [Tailwind CSS](https://tailwindcss.com/) – UI framework  

**Extras**  
- `pypdf`, `python-docx`, `openpyxl` → document parsing  
- *(Image OCR processing will be added in a future update)*  
- `spaCy` or HuggingFace Transformers → NER / metadata extraction  

---


**Project Structure**  

```
document-analysis-rag/
│── backend/
│   ├── manage.py                 # Django management script
│   ├── backend/                  # Django project settings
│   │   ├── __init__.py
│   │   ├── settings.py           # Django settings
│   │   ├── urls.py               # Project URLs
│   │   ├── wsgi.py
│   ├── api/                      # Django app for API
│   │   ├── __init__.py
│   │   ├── models.py             # Django models
│   │   ├── views.py              # API views
│   │   ├── serializers.py        # DRF serializers
│   │   ├── urls.py               # API URLs
│   ├── services/
│   │   ├── parser.py             # PDF/DOCX/Excel parsing
│   │   ├── embeddings.py         # Chunking + embeddings
│   │   ├── vectorstore.py        # FAISS operations
│   │   ├── rag_pipeline.py       # Retrieval + generation
│
│── frontend/
│   ├── pages/                    # Next.js pages
│   ├── components/               # React UI components
│   ├── public/                   # Static assets
│   ├── package.json              # Next.js dependencies
│
│── data/
│   ├── uploads/                  # Uploaded documents
│   ├── faiss_index/              # Vector DB storage
│
│── README.md
│── requirements.txt
```

---

## ⚡ Installation  

### 1. Clone the repo  
```bash
git clone https://github.com/your-username/document-analysis-rag.git
cd document-analysis-rag
```

### 2. Create a virtual environment  
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scriptsctivate      # Windows
```

### 3. Install dependencies  
```bash
pip install -r requirements.txt
```


### 4. Run backend (Django)  
```bash
cd backend
python manage.py migrate
python manage.py runserver
```



### 5. Run frontend (Next.js)  
```bash
cd frontend
npm install
npm run dev
```

---

## 🎯 Usage  

1. Open the frontend UI.  
2. Upload a document (PDF, DOCX, TXT, etc.).  
3. Ask a question in natural language.  
4. Get an **answer with citations** from the uploaded docs.  
5. Optionally, request summaries or export results.  

---

## 🔮 Future Enhancements  
- 📘 Multi-document comparison  
- 🌍 Multilingual support  
- 🧠 Document clustering & topic modeling  
- 🧑‍🤝‍🧑 Role-based dashboards (Legal, Finance, HR views)  
- ⚙️ Agentic workflows (e.g., auto-extract tables → Excel export)  
- 🖼️ Image OCR processing for scanned documents  

---

## 🤝 Contributing  
Contributions are welcome! Please fork the repo and submit a pull request.  

---

## 📜 License  
This project is licensed under the MIT License.  
