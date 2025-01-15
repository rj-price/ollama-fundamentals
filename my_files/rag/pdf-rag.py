# Run `pip install -r requirements.txt` to install the required packages

# 1. Ingest PDF files
# 2. Extract text from PDF files and split into small chunks
# 3. Send chunks to embedding model and save embeddings to a vector database
# 4. Search vector database for similar documents, retrieve and present them to the user


# ==== 1. Ingest PDF files ====

from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader

doc_path ="./data/LRG1_preprint.pdf"
model="llama3.2"

# Local PDF file uploads
if doc_path:
    loader = UnstructuredPDFLoader(file_path=doc_path)
    data = loader.load()
    print("done loading....")
else:
    print("Upload a PDF file")

# Preview first page
content = data[0].page_content
#print(content[:100])

# ==== End of Step 1 ====

###

# ==== 2. Extract text from PDF files and split into small chunks ====

from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# Split and chunk
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
chunks = text_splitter.split_documents(data)
print("done splitting....")

#print(f"Number of chunks: {len(chunks)}")
#print(f"Example chunk: {chunks[0]}")

# ==== End of Step 2 ====

###

# ==== 3. Send chunks to embedding model and save embeddings to a vector database ===

import ollama

ollama.pull("nomic-embed-text")

vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=OllamaEmbeddings(model="nomic-embed-text"),
    collection_name="simple-rag",
)
print("done adding to vector database....")

# ==== End of Step 3 ====

###

# ==== 4. Search vector database for similar documents, retrieve and present them to the user ====

from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever

# set up our model to use
llm = ChatOllama(model=model)

# a simple technique to generate multiple questions from a single question and then retrieve documents
# based on those questions, getting the best of both worlds.
QUERY_PROMPT = PromptTemplate(
    input_variables=["question"],
    template="""You are an AI language model assistant. Your task is to generate five
    different versions of the given user question to retrieve relevant documents from
    a vector database. By generating multiple perspectives on the user question, your
    goal is to help the user overcome some of the limitations of the distance-based
    similarity search. Provide these alternative questions separated by newlines.
    Original question: {question}""",
)

retriever = MultiQueryRetriever.from_llm(
    vector_db.as_retriever(), llm, prompt=QUERY_PROMPT
)

# RAG prompt
template = """Answer the question based ONLY on the following context:
{context}
Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)


chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

#res = chain.invoke(input=("what is the document about?"))
res = chain.invoke(input=("what are the main findings of this research article?"))

print(res)
