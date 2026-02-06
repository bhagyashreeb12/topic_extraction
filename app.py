import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to extract topics using OpenAI API
def extract_topics(text, num_topics):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': f'Extract {num_topics} topics from the following text: {text}'}
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit application
st.title('Topic Extraction from Text Using LLM')

# Input for long text
long_text = st.text_area('Enter long text here:', height=300)

# Input for number of topics
num_topics = st.number_input('Number of topics to extract:', min_value=1, max_value=10, value=3)

# Button to extract topics
if st.button('Extract Topics'):
    if long_text:
        with st.spinner('Extracting topics...'):
            topics = extract_topics(long_text, num_topics)
            st.subheader('Extracted Topics')
            st.write(topics)
    else:
        st.error('Please enter some text to extract topics from.')