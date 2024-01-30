import streamlit as st
from transformers import pipeline
#!pip install sentencepiece
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-tr")

def main():
  st.title("English to Turkish Translator")
  input_text = st.text_input("Enter text in English:")
  if input_text:
    translation = pipe(input_text)[0]["translation_text"]
    st.write("Translation:")
    st.write(translation)

if __name__ == "__main__":
  main()