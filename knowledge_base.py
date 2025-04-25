from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import os

def load_documents(pdf_dir):
    docs = []
    if not os.path.exists(pdf_dir):
        raise FileNotFoundError(f"Directory {pdf_dir} not found.")
    
    for root, _, files in os.walk(pdf_dir):
        for file in files:
            if file.endswith('.pdf'):
                path = os.path.join(root, file)
                print(f"Reading: {path}")
                try:
                    loader = PyPDFLoader(path)
                    docs.extend(loader.load())
                except Exception as e:
                    print(f"Failed to load {path}: {e}")
    return docs

def create_vector_store(docs):
    # Adjust chunk size and overlap for better splitting
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,      # Can hold 1–2 paragraphs or 1 policy section
        chunk_overlap=100     # Ensures transition context between chunks
    )
    split_docs = splitter.split_documents(docs)
    
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(split_docs, embeddings)
    vector_store.save_local("faiss_index")  # Save index
    return vector_store

def get_knowledge_base():
    docs = load_documents("insurance_pdfs")
    return create_vector_store(docs)

if __name__ == "__main__":
    try:
        get_knowledge_base()
        print("Knowledge base created and saved successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")
