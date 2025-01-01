import streamlit as st
import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser

# Add your AI Healthcare Chatbot page content here
def display_ai_assistant():
    st.header(":red[AI Healthcare Chatbot]")
    st.write("Welcome to the AI Healthcare Chatbot page!")

    # Load environment variables
    try:
        load_dotenv()
        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
    except Exception as e:
        st.error(f"Langchain API key or .env file is unavailable at the specified file location.{e}")

    # Check session state for model and messages
    if "llama_model" not in st.session_state:
        st.session_state["llama_model"] = "llama3.1:8b"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Prompt Template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", """You are a knowledgeable and empathetic healthcare assistant. 
             Your role is to provide accurate information and support regarding medical inquiries, patient care, and general health advice. 
             Always prioritize patient safety and confidentiality."""),
            ("user", "Question: {question}")
        ]
    )

    # Display messages in the chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input field for user question
    if user_input := st.chat_input("What's on your mind?"):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        try:
            # Create an LLM instance and parse the output
            llm = Ollama(model=st.session_state["llama_model"])
            output_parser = StrOutputParser()
            chain = prompt | llm | output_parser

            # Invoke the chain and get the assistant's response
            assistant_response = chain.invoke({"question": user_input})

            with st.chat_message("assistant"):
                st.markdown(assistant_response)

            st.session_state.messages.append({"role": "assistant", "content": assistant_response})

        except Exception as e:
            st.error(f"LLaMA model (LLaMA 3.1: 8B) is unavailable. Please install it.{e}")

# Call the display function to show the AI Assistant
if __name__ == "__main__":
    display_ai_assistant()
