import streamlit as st

st.header("🧐Como Funciona o Tradutor de Queries?🧐")
st.text("""O tradutor de queries é uma ferramenta baseia na biblitoeca de código aberto sqlglobt,
e executa determinados algoritmos que são responsáveis por realizar o parse(conversão) de expressões
de diferentes bancos de dados.

Por ser uma ferramenta Open Source e estar em constante desenvolvimento, alguns erros de sintaxe podem
passar despercebidos. Por isso é importante que as consultas sejam testadas após a conversão.

Caso você indentifique alguma consulta que foi traduzida incorretamente, por favor nos envie-a e iremos
sinalizar esse erro no repositório da ferramenta :) Entretanto, a princípio essa biblioteca tem recebido
bons elogios.""")

st.subheader("""
🔥Como usar essa ferramenta?🔥
""")

st.text("""
No menu lateral, selecione a página do Tradutor.
Nessa página serão pedidas algumas informações.
""")

st.text("""
A primeira caixa se refere a sintaxe da consulta que você deseja converter, ou seja,
em qual banco de dados você estava realizando a consulta.
""")

st.text("""
A segunda caixa se refere para qual sintaxe você deseja converter a consulta, ou seja,
em qual banco de dados você deseja executar a consulta atualmente.
""") 

st.text("""
Na terceira caixa, insira a consulta que deseja traduzir e em seguida aperte o botão traduzir.
Será exibido na tela o resultado da conversão, e então é só copiar e colar na sua ferramenta
de acesso ao banco de dados.
"""
)