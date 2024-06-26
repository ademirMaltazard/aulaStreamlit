import pandas
import streamlit as st
import plotly.express as px

df = pandas.read_csv('https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv')
grafico = px.pie(df, names="Popularidade", hole=0.7)
grafico2 = px.bar(df, color="Desenvolvedores", x="Linguagem", y="Popularidade")

st.markdown("# Tipos de graficos com plotly")

st.plotly_chart(grafico)
st.plotly_chart(grafico2)

st.write("## mostrando o Dieguin")

pagina1, pagina2 = st.tabs(["pagina1", "pagina2"])

with pagina1:
    st.image(r"./image/Dieguin.jpeg", width=300)

with pagina2:
    st.video("https://www.youtube.com/shorts/7J-zTyYaE8Y?feature=share")
