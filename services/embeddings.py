from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from services.tableau_mcp import get_tableau_metadata
from config_utils import get_config_value
import os

CHROMA_DIR = "./data/vectorstore"

def is_chroma_index_ready() -> bool:
    if not os.path.isdir(CHROMA_DIR):
        return False

    try:
        subdirs = [d for d in os.listdir(CHROMA_DIR) if os.path.isdir(os.path.join(CHROMA_DIR, d))]
        for d in subdirs:
            folder = os.path.join(CHROMA_DIR, d)
            if all(os.path.exists(os.path.join(folder, fname)) for fname in ["data_level0.bin", "header.bin"]):
                return True
        return False
    except Exception:
        return False


def build_vector_store():
    metadata = get_tableau_metadata()
    texts = [item["text"] for item in metadata]
    metadatas = [{"source": item["source"]} for item in metadata]

    embeddings = OpenAIEmbeddings(openai_api_key=get_config_value("OPENAI_API_KEY"))
    vectordb = Chroma.from_texts(texts=texts, embedding=embeddings, metadatas=metadatas, persist_directory=CHROMA_DIR)
    vectordb.persist()
    return vectordb

def load_vector_store():
    if not os.path.exists(CHROMA_DIR):
        raise FileNotFoundError("⚠️ Chroma vector store not found. Run `build_index.py` first.")
    embeddings = OpenAIEmbeddings(openai_api_key=get_config_value("OPENAI_API_KEY"))
    return Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)

def semantic_search_with_justification(query, k=3):
    vectordb = load_vector_store()
    return vectordb.similarity_search_with_score(query, k=k)
