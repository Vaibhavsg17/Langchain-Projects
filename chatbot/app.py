from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st 
import os 
from dotenv import load_dotenv

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
st.title("Langchain Demo With OPENAI API")
input_text=st.text_input("Search the topic u want")

# openAI LLm

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
