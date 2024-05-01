import streamlit as st
import pandas

st.title('minha primeira pagina :wolf:')

st.write('''
    Teste de escrita com comando write
    
    #### Exibindo dados:
''')

df = pandas.read_csv('https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv')
st.dataframe(df)

st.write('#### Teste de selectbox')
result = st.selectbox('qual sua maneira de contato ideal:', ['telefone', 'celular', 'email'])
st.write(result)

st.write('#### Primeiro uso de selectbox para filtragem de dados:')
linguagem = st.selectbox("selecione a linguagem", df['Linguagem'].unique())

if st.button('Filtrar por linguagem'):
    df.loc[df["Linguagem"] == linguagem]
