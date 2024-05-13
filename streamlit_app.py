
#streamlit_app.py
import streamlit as st
import requests

def main():
    st.title('Interface de Análise de Sentimento')
    user_input = st.text_area('Digite um texto para analisar o sentimento:', height=150)
    if st.button('Analisar Sentimento'):
        response = requests.post('http://localhost:8000/predict', json={'text': user_input})
        if response.status_code == 200:
            st.write('Resultado da análise:')
            st.write(response.json())
        else:
            st.error('Falha ao processar a solicitação.')

if __name__ == '__main__':
    main()

