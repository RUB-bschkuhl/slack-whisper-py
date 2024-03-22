import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from flask import jsonify
from openai import OpenAI

load_dotenv() 

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def generate_suggestions(prompt_template, transcript, gpt="gpt-3.5-turbo"):
    # print("Generating suggestions")
    
    prompt = f"""
    Transcript:
    {transcript}
    -------------
    Input:
    {prompt_template} 
    """

    from openai import OpenAI
    client = OpenAI()

    completion = client.chat.completions.create(
    model=gpt,
    messages=[
        {"role": "system", "content": "You are a helpfull assistant."},
        {"role": "user", "content": prompt}
    ]
    )

    print(prompt,completion)
    
    return completion.choices[0].message.content

def generate_suggestions_local(prompt_template, transcript):

    prompt = f"""
    Transcript:
    {transcript}
    -------------
    Input:
    {prompt_template} 
    """
        
    # Point to the local server
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

    completion = client.chat.completions.create(
    model="local-model", # this field is currently unused
    messages=[
        {"role": "system", "content": "Always answer in rhymes."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.1,
    )

    return completion.choices[0].message.content