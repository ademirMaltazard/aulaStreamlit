import streamlit as st
import pandas

csv_dados = pandas.read_csv('https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv')
st.write('## EXIBIÇÃO MICRODADOS SOBRE POPULARIDADE POR LINGUAGEM DE PROGRAMAÇÃO')
st.write('Pagina para teste de exibição de dados em formato de graficos.')

st.bar_chart(csv_dados, x='Linguagem', y='Desenvolvedores')
st.scatter_chart(csv_dados, x='Linguagem', y='Desenvolvedores')
st.line_chart(csv_dados, x='Linguagem', y='Desenvolvedores')
st.area_chart(csv_dados, x='Linguagem', y='Desenvolvedores')
st.bar_chart(csv_dados, x='Popularidade', y='Desenvolvedores', color="Desenvolvedores")
