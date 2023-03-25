import streamlit as st
import os
import openai
import requests
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("""✍️Tradutor de Queries""")




def make_translation():
    source_type = st.selectbox(label='Selecione a sintaxe utilizada na consulta',
                               options=['Redshift','BigQuery','MySql','Postgresql', 'SparkSQL'])

    destination_type = st.selectbox(label='Selecione para qual tipo de banco de dados deseja traduzir',
                                    options= ['Redshift','BigQuery','MySql','Postgresql', 'SparkSQL'])

    source_query = st.text_area(label='Digite a query que deseja traduzir')

    return [source_type,destination_type,source_query]


translation_parameters = make_translation()




if st.button('Traduzir'):

    ask = f'just give me this {translation_parameters[0]} query "{translation_parameters[2]}" in {translation_parameters[1]} sintaxe without explanations'
    request = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role":"user", "content": ask}
        ]
    )
    st.subheader('Resultado da Tradução')
    

    st.text(request['choices'][0]['message']['content'])
