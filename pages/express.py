import pandas
import streamlit as st
import plotly.express as px

df = pandas.read_csv('https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv')
grafico = px.pie(df, names="Popularidade")
grafico2 = px.bar(df, color="Desenvolvedores", x="Linguagem", y="Popularidade")

st.markdown("# Tipos de graficos com plotly")

st.plotly_chart(grafico)
st.plotly_chart(grafico2)

st.write("## mostrando o Dieguin")

pagina1, pagina2 = st.tabs(["pagina1", "pagina2"])

with pagina1:
    st.image("../image/Dieguin.jpeg")

with pagina2:
    st.video("https://www.youtube.com/shorts/7J-zTyYaE8Y?feature=share")