import os
import time
import fitz  # PyMuPDF
from langchain_community.vectorstores import Pinecone as PineconeVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Cargar variables de entorno
load_dotenv()

# Inicializar Pinecone con su clave de API
pinecone_api_key = os.getenv("PINECONE_API_KEY")
if not pinecone_api_key:
    raise ValueError("Añadir la api key con el nombre: PINECONE_API_KEY")

# Configurar el cliente de Pinecone
pc = Pinecone(api_key=pinecone_api_key)

# Especificar el cloud y la región
cloud = os.getenv('PINECONE_CLOUD', 'aws')
region = os.getenv('PINECONE_REGION', 'us-east-1')
spec = ServerlessSpec(cloud=cloud, region=region)

# Nombre del índice
index_name = "taskmov"

# Conectar al índice o crearlo si no existe
existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]
if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=spec
    )
    while not pc.describe_index(index_name).status['ready']:
        time.sleep(1)
index = pc.Index(index_name)

# Configurar embeddings (modelo con una dimensión de 384)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Crear vector_store y conectar al índice Pinecone
vector_store = PineconeVectorStore.from_existing_index(index_name, embeddings)

# Leer el archivo PDF y extraer el texto
pdf_path = "C:/Users/Jessica/Downloads/Propuestas.pdf"
doc_text = ""

with fitz.open(pdf_path) as pdf:
    for page in pdf:
        doc_text += page.get_text() + "\n"

# Dividir el texto en chunks utilizando RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
     separators=["\n\n", "\n", ".", " "],  # Separador utilizado en los documentos
    chunk_size=800,
    chunk_overlap=100,
    length_function=len
)

chunks = text_splitter.split_text(doc_text)
print(chunks)

# Crear vector_store y almacenar chunks de texto con sus incrustaciones en el índice Pinecone
vector_store = PineconeVectorStore.from_texts(chunks, embeddings, index_name=index_name)