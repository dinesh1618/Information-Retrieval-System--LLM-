import os
from dotenv import load_dotenv
from pathlib import Path
from ensure import ensure_annotations
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import GooglePalmEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import GooglePalm

load_dotenv()
os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')

@ensure_annotations
def PDFLoader(doc_path: Path) -> list:
    doc_path = Path(doc_path)
    loader = PyPDFLoader(doc_path)
    return loader.load()

@ensure_annotations
def TextSplitter(list_docs: list, chunk_size=800, chunk_overlap=50) -> list:
    text_spltter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_spltter.split_documents()

@ensure_annotations
def VectorStore(list_splitdocs: list):
    embeddings = GooglePalmEmbeddings()
    return FAISS.from_documents(documents=list_splitdocs, embedding=embeddings)
