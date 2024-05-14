
#streamlit_app.py
import streamlit as st
import requests

def main():
    st.title('Sentiment Analysis Interface')
    user_input = st.text_area('Type a text to analyze sentiment:', height=150)
    if st.button('Analyze Sentiment'):
        response = requests.post('http://localhost:8000/predict', json={'text': user_input})
        if response.status_code == 200:
            st.write('Analysis Result:')
            st.write(response.json())
        else:
            st.error('Failed to process the request.')

if __name__ == '__main__':
    main()


