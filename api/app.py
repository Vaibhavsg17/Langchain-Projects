from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import os
import uvicorn
from langchain_community.llms import Ollama
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="LangChain Server", version="1.0", description="Simple API server")


# Home route
@app.get("/")
def read_root():
    return {"message": "Welcome to the LangChain API!"}


add_routes(
    app,
    ChatOpenAI(),
    path="/chat",
)

model = ChatOpenAI()
llm = Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template(
    "write me an essay about {topic} with 100 words"
)
prompt2 = ChatPromptTemplate.from_template(
    "write me a poem about {topic} with 100 words"
)

add_routes(
    app,
    prompt1 | model,
    path="/essay",
)

add_routes(
    app,
    prompt2 | llm,
    path="/poem",
)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=8000,
    )
