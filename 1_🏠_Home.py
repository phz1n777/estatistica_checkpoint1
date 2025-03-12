import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo


# Configuração da página
st.set_page_config(page_title="Dashboard de Distribuições Probabilísticas", layout="wide")
st.sidebar.markdown("Desenvolvido por Prof. Tiago Marum [THM Estatística](https://thmestatistica.com)")

# Adicionando logo com streamlit-extras
# add_logo("logo.jpeg")

# Adicionando o logo
st.logo("logo.png")

# Adicionando o logo no body
# st.image("mamaco.png", width=250)

st.title("Pedro Henrique de Assunção Lima")
st.header("Quem sou eu?", divider="gray")

st.write("Sou um estudante de Engenharia de Software da Faculdade de Informatica e Administração Paulista (FIAP), apaixonado por tecnologia e programação, gosto de música, esportes e carros. Tenho 20 anos, não tive nenhuma experiencia profissional, mas busco oportunidades para o meu aprendizado.")


st.header("Educação", divider="gray")
st.write("### Colegio Piccneli")
st.write("2010 - 2015 | Ensino Fundamental 1")
st.write("### Colégio São Luiz Anglo")
st.write("2016 - 2019 | Ensino Fundamental 2 \n\n 2020 - 2022 | Ensino Médio")

st.write("### FIAP - Faculdade de Informatica e Administração Paulista")
st.write(" 2023 - Atual | Engenharia de Software \n\n Conclusão: 2027")

st.divider()

st.subheader("Contato")
st.write("Email: phassuncaolima7@gmail.com")
st.write("Telefone: (11)97198-4392")


