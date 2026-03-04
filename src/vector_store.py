import os

os.environ.setdefault("TRANSFORMERS_NO_TF", "1")
os.environ.setdefault("USE_TF", "0")

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
import pandas as pd

from dotenv import load_dotenv
load_dotenv()

class VectorStoreBuilder:
    def __init__(self,csv_path:str,persist_dir:str="chroma_db"):
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        self.embedding = HuggingFaceEmbeddings(model_name = "all-MiniLM-L6-v2")
    
    def build_and_save_vectorstore(self):
        df = pd.read_csv(self.csv_path, encoding='utf-8').dropna()
        data = [
            Document(page_content=row["combined_info"], metadata={"row": idx})
            for idx, row in df.iterrows()
        ]

        db = Chroma.from_documents(data,self.embedding,persist_directory=self.persist_dir)
        db.persist()

    def load_vector_store(self):
        return Chroma(persist_directory=self.persist_dir,embedding_function=self.embedding)



