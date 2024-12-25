from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
# Langmith tacking
os.environ['OPENAI_API_KEY']="true"
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")

# Promt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful AI assistant, please response to the user queries"),
        ("user","Question:{question}"),
    ]
)

# streamlit framework 
st.title("Langchain Demo With Ollama")
input_text=st.text_input("Search the topic u want")

# ollama llama2 LLm

llm = Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
