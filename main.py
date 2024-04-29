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

if st.button('Filtrar por linguagem'):
    df.loc[df["Linguagem"] == linguagem]

#--------------------------------------------------------------------------------------

st.write('## EXIBIÇÃO MICRODADOS SOBRE VIOLÊNCIA')

csv_violence = pandas.read_csv("https://raw.githubusercontent.com/natorjunior/pandas/main/Aula-02/microdados_violencia_reduzido.csv")
# df_violence = st.dataframe(csv_violence)

uf = st.selectbox('selecione a UF:', csv_violence['id_uf_ocorrencia'].unique())
button_fill = st.button('filtrar')

if button_fill:
    st.write('### dados filtrados por uf:')
    fill_uf = csv_violence.loc[csv_violence['id_uf_ocorrencia'] == uf]
    st.dataframe(fill_uf)

    st.write('### dados filtrados por tipo de arma:')
    st.dataframe(fill_uf.loc[fill_uf['meio_arma_fogo'] == 0])
