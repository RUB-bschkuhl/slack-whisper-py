import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_agent_executor
from dotenv import load_dotenv
from flask import  jsonify

load_dotenv() 

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def generate_suggestions(prompt_template, transcript):
    print("Generating suggestions")
    
    prompt = f"""
    {transcript}
    -------------
    {prompt_template} 
    """
    llm = ChatOpenAI(model="gpt-3.5-turbo-preview" temperature=0.5, max_tokens=100, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0, stop=["\n"])
    llm.set_api_key(OPENAI_API_KEY)
    response = llm.generate(prompt, max_tokens=100)
    print(response)
    suggestion = response.choices[0].text.strip()
    
    out = ""
    suggestion += str(out)
    return jsonify({"suggestion": suggestion})