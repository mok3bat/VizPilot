from services.embeddings import build_vector_store

if __name__ == "__main__":
    build_vector_store()
    print("✅ Vector DB created and persisted.")
