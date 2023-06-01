import os
import openai
import gradio as gr

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual OpenAI API key

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

def openai_create(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return response.choices[0].text

def chatgpt_clone(input, history):
    history = history or []
    history.append(("Human:", input))
    inp = ' '.join(sum(history, ()))
    output = openai_create(inp)
    history.append(("AI:", output))
    return history, history

block = gr.Interface(
    fn=chatgpt_clone,
    inputs=["text", "text[]"],
    outputs=["text[]", "text[]"],
    title="Build Your Own ChatGPT",
    description="An interactive chatbot powered by OpenAI GPT-3",
    article="https://github.com/openai/openai-cookbook/blob/main/examples/How_to_build_a_chatbot_with_GPT3.ipynb",
    examples=[
        ["What's the weather today?", "It's sunny and 75 degrees."],
        ["Tell me a joke.", "Why don't scientists trust atoms? Because they make up everything!"],
    ],
    allow_flagging=False,
)

block.launch()
