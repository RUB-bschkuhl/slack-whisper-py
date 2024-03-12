import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from flask import jsonify

load_dotenv() 

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def generate_suggestions(prompt_template, transcript):
    # print("Generating suggestions")
    
    prompt = """
    Transcript:
    {transcript}
    -------------
    Input:
    {prompt_template} 
    """

    # llm = ChatOpenAI(model="gpt-4-turbo",
    #                   api_key=OPENAI_API_KEY)
    # response = llm.invoke(prompt)
    # suggestion = response.choices[0].text.strip()
    from openai import OpenAI
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpfull assistant."},
        {"role": "user", "content": prompt}
    ]
    )

    print(completion.choices[0].message.content)
    
    return completion.choices[0].message.content