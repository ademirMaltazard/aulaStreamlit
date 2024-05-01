import streamlit as st
import pandas

csv_violence = pandas.read_csv("https://raw.githubusercontent.com/natorjunior/pandas/main/Aula-02/microdados_violencia_reduzido.csv")
st.write('## EXIBIÇÃO MICRODADOS SOBRE VIOLÊNCIA')

st.write('Pagina para exbição de dados ultilizando filtro.')
st.write('OBS: Esta página pode demorar a carregar um pouco.')

uf = st.selectbox('selecione a UF:', csv_violence['id_uf_ocorrencia'].unique())
button_fill = st.button('filtrar')

if button_fill:
    st.write('### dados filtrados por uf:')
    fill_uf = csv_violence.loc[csv_violence['id_uf_ocorrencia'] == uf]
    st.dataframe(fill_uf)

    st.write('### dados filtrados por tipo de arma:')
    st.dataframe(fill_uf.loc[fill_uf['meio_arma_fogo'] == 0])
