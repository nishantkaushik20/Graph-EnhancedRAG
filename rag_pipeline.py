from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from graph_builder import load_graphml
import config

from langchain_community.chat_models import AzureChatOpenAI
import config

def get_llm():
    return AzureChatOpenAI(
        azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
        openai_api_key=config.AZURE_OPENAI_API_KEY,
        openai_api_version=config.AZURE_OPENAI_API_VERSION,
        deployment_name=config.AZURE_DEPLOYMENT_NAME,
        temperature=config.TEMPERATURE
    )


def load_graph_context(query, graph_path='graph/context_graph.graphml'):
    graph = load_graphml(graph_path)
    context_nodes = [n for n in graph.nodes if query.lower() in n.lower()]
    context = ""
    for node in context_nodes:
        context += graph.nodes[node].get("content", "") + "\n"
    return context.strip()

def run_graph_rag(query, retriever, graph_context):
    llm = get_llm()
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )
    combined_query = f"{graph_context}\n\nUser Query: {query}"
    return qa_chain.run(combined_query)