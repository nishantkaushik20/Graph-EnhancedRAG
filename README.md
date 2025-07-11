# Graph-Enhanced RAG 🔍🧠

This project is a practical implementation of Retrieval-Augmented Generation (RAG), enhanced with a knowledge graph layer. By combining GraphML, LangChain, vector databases, and OpenAI (or Azure OpenAI), the system generates more context-aware and reliable responses from LLMs.

I built this as a way to explore how adding graph-based structure to unstructured data can improve the quality of answers — especially in edge cases where normal RAG pipelines fall short.

---

## 🔧 What It Does

- Uses a knowledge graph (via `networkx`) to extract relevant context
- Supports both OpenAI and Azure OpenAI backends
- Implements FAISS or Chroma as vector stores
- Combines retrieved vector chunks + graph-based context before hitting the LLM
- CLI-based and Streamlit-ready (your choice)

---

## 🗂 Project Structure

```
graph_enhanced_rag/
├── app.py                  # CLI entrypoint
├── config.py               # Loads .env and keys
├── rag_pipeline.py         # Core RAG + LLM logic
├── graph_builder.py        # GraphML-based context engine
├── requirements.txt
├── .env                    # API keys (not committed)
├── README.md
├── .gitignore
├── data/documents/         # Input text files
├── graph/context_graph.graphml
└── outputs/logs/           # Optional logging folder
```

---

## 🚀 How to Run It (CLI)

1. Clone this repo and navigate into it:

   ```bash
   git clone https://github.com/yourname/graph-enhanced-rag.git
   cd graph-enhanced-rag
   ```

2. Set up your environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API keys:

   ```
   AZURE_OPENAI_API_KEY=your-key-here
   AZURE_OPENAI_ENDPOINT=https://your-endpoint
   AZURE_DEPLOYMENT_NAME=gpt4omini
   AZURE_OPENAI_API_VERSION=2024-08-01-preview

   AZURE_EMBEDDING_DEPLOYMENT=embedding-model-name
   ```

4. Run the CLI app:

   ```bash
   python app.py
   ```

---

## ⚙️ Tech Stack

- **LangChain**
- **Azure OpenAI / OpenAI**
- **FAISS**
- **GraphML (networkx)**
- **Python**

---

## 💡 Why I Built This

I was exploring how LLMs could perform better with structured context, especially in use cases like finance, healthcare, or long documents. This is my attempt at making RAG smarter by injecting graph-based relationships into the prompt without fine-tuning the LLM itself.

---

## 📄 License

MIT — feel free to use or extend it.

---

## 🙌 Contributions

Not open for PRs right now, but feel free to fork and build on top of this!
