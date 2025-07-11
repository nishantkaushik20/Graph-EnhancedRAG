from rag_pipeline import run_graph_rag, load_graph_context
from langchain.vectorstores import FAISS
from langchain_community.embeddings import AzureOpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, AZURE_DEPLOYMENT_NAME, AZURE_OPENAI_API_VERSION, USE_AZURE
import os
import sys

def main():
    if not USE_AZURE:
        print("❌ This version is configured for Azure only. Please set USE_AZURE=True in config.py.")
        sys.exit(1)

    query = input("Enter your question: ").strip()
    if not query:
        print("⚠️  No query provided.")
        return

    file_path = "data/documents/sample.txt"
    if not os.path.exists(file_path):
        print(f"❌ ERROR: Source file not found: {file_path}")
        return

    print("📄 Loading documents...")
    loader = TextLoader(file_path)
    docs = loader.load()

    if not docs:
        print("⚠️ No documents loaded.")
        return

    print("🔍 Splitting text and embedding...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    deployment=AZURE_DEPLOYMENT_NAME,
    openai_api_key=AZURE_OPENAI_API_KEY,
    openai_api_version=AZURE_OPENAI_API_VERSION,
    chunk_size=512  # ✅ Explicitly set a valid chunk size (max 2048)
)

    vectordb = FAISS.from_documents(chunks, embeddings)

    print("🔗 Loading graph context...")
    graph_context = load_graph_context(query)

    print("⚙️ Running RAG pipeline...")
    result = run_graph_rag(query, vectordb.as_retriever(), graph_context)

    print("\n✅ Answer:")
    print(result)

if __name__ == "__main__":
    main()
