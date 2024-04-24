import streamlit as st
import pandas

print('console')

st.title('minha primeira pagina :wolf:')

st.write('''
    Teste de escrita com comando write
''')
df = pandas.read_csv('https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv')

st.dataframe(df)

result = st.selectbox('qual sua maneira de contato ideal:', ['telefone', 'celular', 'email'])

st.write(result)



linguagem = st.selectbox("selecione a linguagem", df['Linguagem'].unique())

if st.button('Filtrar'):
    df.loc[df["Linguagem"] == linguagem]
