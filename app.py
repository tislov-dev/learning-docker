import streamlit as st
from transformers import pipeline
import pandas as pd

st.title('Question Answering')

@st.cache(allow_output_mutation=True)
def load_model():
    return pipeline('question-answering')

nlp = load_model()
def main():
    question = st.text_area('Enter your question here!', 'What is my name?')
    context = st.text_area('Enter your context here!', 'My name is Alice and I live in Ireland.')
    # nlp = load_model()
    results = nlp(question=question, context=context)
    st.write(results['answer'])

if __name__== '__main__':
    main()






