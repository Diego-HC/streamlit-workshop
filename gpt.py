from openai import OpenAI
import streamlit as st

openai_key = st.secrets["OPENAI_KEY"]
client = OpenAI(api_key=openai_key)


def gpt_wrapper_message(prompt: str):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "developer", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    return completion.choices[0].message.content
