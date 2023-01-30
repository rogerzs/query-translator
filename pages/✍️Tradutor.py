import streamlit as st
import sqlglot as sg

st.title("""✍️Tradutor de Queries""")

def make_translation():
    source_type = st.selectbox(label='Selecione a sintaxe utilizada na consulta',
                               options=['Redshift','BigQuery','MySql','Postgresql'])

    destination_type = st.selectbox(label='Selecione para qual tipo de banco de dados deseja traduzir',
                                    options= ['Redshift','BigQuery','MySql','Postgresql'])

    source_query = st.text_area(label='Digite a query que deseja traduzir')

    return [source_type,destination_type,source_query]


translation_parameters = make_translation()

if st.button('Traduzir'):

    st.subheader('Resultado da Tradução')

    st.text(sg.transpile(translation_parameters[2],
                        write=translation_parameters[1].lower(),
                        read=translation_parameters[0].lower(),
                        pretty = True
                        )[0]
    )
