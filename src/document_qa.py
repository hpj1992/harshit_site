from langchain_core.text_splitters import RecursiveCharacterTextSplitter
from langchain_core.embeddings import HuggingFaceEmbeddings
from langchain_core.vectorstores import Chroma
from langchain_core.chains import RetrievalQA
from langchain_core.llms import LlamaCpp
from langchain_core.documents import Document
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# 1. Load the document
def load_document(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    return ["""""" + content + """"""]

# 2. Split the document
def split_text(documents):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)
    return texts

# 3. Create vector store
def create_vector_store(texts):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = Chroma.from_documents(texts, embeddings)
    return vectorstore

# 4. Create QA chain
def create_qa_chain(vectorstore):
    llm = LlamaCpp(
        model_path="/Users/hpjoshi/Documents/AppliedAI/llama.cpp/build/models/llama-2-7b-chat.ggmlv3.q4_K_M.bin",
        n_ctx=2048,
        n_threads=8,
        n_batch=512,
        temperature=0.7,
        max_tokens=2000
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    return qa_chain

# Main function
def main():
    # Load and process the document
    file_path = "../../data/sample.txt"
    documents = load_document(file_path)
    texts = split_text(documents)
    vectorstore = create_vector_store(texts)
    qa_chain = create_qa_chain(vectorstore)

    # Ask questions
    while True:
        question = input("\nEnter your question (or type 'quit' to exit): ")
        if question.lower() == 'quit':
            break
        answer = qa_chain.run(question)
        print("\nAnswer:", answer)

if __name__ == "__main__":
    main()
