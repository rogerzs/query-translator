import streamlit as st
import sqlglot as sg
import os
import openai
import requests

openai.organization = "org-lDJkFWdxGIFzrvtdi6k4eqOK"
openai.api_key = os.getenv("OPEN_API_KEY")

st.title("""✍️Tradutor de Queries""")

source_type = ''
destination_type = ''
source_query = ''

def make_translation():
    source_type = st.selectbox(label='Selecione a sintaxe utilizada na consulta',
                               options=['Redshift','BigQuery','MySql','Postgresql'])

    destination_type = st.selectbox(label='Selecione para qual tipo de banco de dados deseja traduzir',
                                    options= ['Redshift','BigQuery','MySql','Postgresql'])

    source_query = st.text_area(label='Digite a query que deseja traduzir')

    return [source_type,destination_type,source_query]


translation_parameters = make_translation()

if st.button('Traduzir'):

    request = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role":"user", "content":f"Converta a query abaixo de {source_type} para {destination_type} \n {source_query}"}
        ]
    )
    st.subheader('Resultado da Tradução')

    st.text(request)
