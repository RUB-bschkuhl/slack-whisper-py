import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from flask import jsonify

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