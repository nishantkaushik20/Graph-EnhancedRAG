# Graph-Enhanced RAG 🧠🔍

This is a proof-of-concept project that enhances Retrieval-Augmented Generation (RAG) with a knowledge graph using GraphML. The system leverages LangChain, OpenAI or Azure OpenAI APIs, and graph structures to improve context relevance and reduce hallucination in LLM outputs.

## 🔧 Features

- Dynamic knowledge graph context extraction with `networkx`
- Integration with `LangChain` and `OpenAI` for RAG
- Supports both FAISS and Chroma vector stores
- Streamlit app for easy interaction
- Configurable for OpenAI or Azure OpenAI backends

## 📁 Project Structure

```
graph_enhanced_rag/
├── app.py
├── config.py
├── graph_builder.py
├── rag_pipeline.py
├── requirements.txt
├── .env               # DO NOT COMMIT THIS
├── README.md
├── .gitignore
├── data/
│   └── documents/
│       └── sample.txt
├── graph/
│   └── context_graph.graphml
└── outputs/
    └── logs/
```

## 🚀 How to Run

1. Clone the repo and `cd graph_enhanced_rag`
2. Create a `.env` file using `.env.example` or manually set:
```
OPENAI_API_KEY=your-key
AZURE_OPENAI_API_KEY=your-key
AZURE_OPENAI_ENDPOINT=https://your-endpoint/
```
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run app.py
```

## 🛠 Tech Stack

- Python
- LangChain
- OpenAI / Azure OpenAI
- FAISS
- NetworkX (GraphML)

## 📄 License

This project is licensed under the MIT License.
