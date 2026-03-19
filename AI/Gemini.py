import streamlit as st
from PIL import Image
import os
import pathlib
import textwrap

os.environ['GEMINI_API_KEY'] = 'YOur api key'

import google.generativeai as genai

genai.configure(api_key=os.environ['GEMINI_API_KEY'])


def get_gemini_response(input, image):
    model = genai.GenerativeModel("models/gemini-3-flash-preview")

    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content([image])

    return response.text

st.set_page_config(page_title="Gemini-3 LLM", page_icon="🤖", layout="wide")

st.header("🤖 Gemini-3 LLM")
input = st.text_input('Input prompt:', key='input')

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Upload Image.', use_column_width=True)

submit = st.button('Generate Response about the image')

if submit:
    responce = get_gemini_response(input, image)
    st.subheader("Gemini-3 LLM Response:")
    st.write(responce)