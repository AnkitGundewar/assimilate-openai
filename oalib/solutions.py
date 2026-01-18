"""Library with OpenAI API solutions as functions

References:

For building code:  https://beta.openai.com/docs/guides/code/introduction

"""
#Library with OpenAI API solutions as functions.

from openai import OpenAI

client = OpenAI()


def submit_question(text: str) -> str:
    """Submit a question to the OpenAI API and return the answer."""
    resp = client.responses.create(
        model="gpt-4.1-mini",
        input=text,
        temperature=0,
        max_output_tokens=300,
    )
    return resp.output_text.strip()


def create_code(text: str, language: str) -> str:
    """Convert a comment into code in a given language."""
    prompt = f"Write {language} code for the following request:\n{text}\nReturn only code."
    resp = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        temperature=0,
        max_output_tokens=300,
    )
    return resp.output_text.strip()
