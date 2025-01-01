import streamlit as st
import os
from dotenv import load_dotenv
import asyncio

# LangChain and other dependencies
from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import RetrievalQA

# Add your AI Report Analyzer page content here
def display_report_analyzer():
    st.header(":red[AI Report Analyzer]")
    st.write("Welcome to the AI Report Analyzer page!")
    
    # Sidebar for data source selection
    st.sidebar.header("Lab Report Data Source")

    # Load environment variables
    try:
        load_dotenv()
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
    except Exception as e:
        st.error(f"Langchain API key or .env file is unavailable at the specified file location.{e}")

    # Initialize session state variables
    if "llama_model" not in st.session_state:
        st.session_state["llama_model"] = "llama3.1:8b"
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "knowledge_base" not in st.session_state:
        st.session_state.knowledge_base = None

    # Load the language model
    llm = Ollama(model=st.session_state["llama_model"], temperature=0)
    output_parser = StrOutputParser()
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", '''You are a knowledgeable healthcare assistant. 
             Your role is to provide accurate information and support regarding medical inquiries Please respond to user queries.'''),
            ("user", "query: {question}")
        ]
    )
    chain = prompt_template | llm | output_parser

    # Function to set up the QA retrieval chain
    def setup_retrieval_qa_chain(knowledge_base):
        return RetrievalQA.from_chain_type(chain, retriever=knowledge_base.as_retriever())

    # Load data and create embeddings
    def process_text(text):
        text_splitter = CharacterTextSplitter.from_tiktoken_encoder(
            encoding_name="cl100k_base", chunk_size=1000, chunk_overlap=250
        )
        texts = text_splitter.split_text(text)
        embeddings = HuggingFaceEmbeddings()
        documents = [Document(page_content=chunk) for chunk in texts]
        return FAISS.from_documents(documents, embeddings)

    # PDF Loader
    uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type="pdf")
    if uploaded_file:
        with st.spinner("Processing PDF..."):
            try:
                # Save the uploaded file temporarily
                with open(uploaded_file.name, "wb") as f:
                    f.write(uploaded_file.getbuffer())

                # Load the PDF using PyPDFLoader
                loader = PyPDFLoader(uploaded_file.name)
                pages = []
                
                async def load_pdf_pages():
                    async for page in loader.alazy_load():
                        pages.append(page)
                
                asyncio.run(load_pdf_pages())

                # Combine all page contents into a single string
                combined_text = ''.join(page.page_content for page in pages)
                st.session_state.knowledge_base = process_text(combined_text)
                
                st.success("PDF Uploaded Successfully! Data Extraction and Knowledge Base Creation Complete")
                
                # Optionally, delete the file after processing
                os.remove(uploaded_file.name)
            except Exception as e:
                st.error(f"Error loading PDF: {e}")

    # Check if knowledge base is loaded
    qa_chain = None
    if st.session_state.knowledge_base:
        qa_chain = setup_retrieval_qa_chain(st.session_state.knowledge_base)

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chatbot interface
    if user_input := st.chat_input("What's on your mind?"):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Get response from the RAG application
        if qa_chain:
            try:
                response = qa_chain.invoke({"query": user_input})['result']
                with st.chat_message("assistant"):
                    st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Error in processing query: {e}")
        else:
            st.error("No knowledge base loaded. Please upload a PDF ")

# Call the display function to show the AI Report Analyzer
if __name__ == "__main__":
    display_report_analyzer()