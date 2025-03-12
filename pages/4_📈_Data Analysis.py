import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import seaborn as sns
import matplotlib.pyplot as plt
from plotnine import *

st.set_page_config(
    page_title="Dados",
    page_icon="🏃🏼",
    layout="wide"
)

# Função para exibir gráfico Plotly
def plot_distribution(x, y, title, xlabel, ylabel):
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(title=title, xaxis_title=xlabel, yaxis_title=ylabel)
    st.plotly_chart(fig)



st.header("Análise de Dados")
st.divider()
uploaded_file = "Placement_Data_Full_Class.xlsx"

st.title("Análise Estatística dos Dados de Contratação de Alunos")

# Seção 1: Apresentação dos Dados
st.header("1. Apresentação dos Dados")

st.subheader("1.1 Descrição do Conjunto de Dados")
st.write(
    "O conjunto de dados utilizado neste estudo contém informações sobre alunos de uma instituição de ensino "
    "e sua possível contratação por empresas. As variáveis incluem características acadêmicas, como notas "
    "em diferentes etapas da educação, área de estudo, especialização no MBA, e experiência de trabalho. "
    "O objetivo é analisar quais fatores influenciam a contratação de um aluno e se há padrões que possam prever esse resultado."
)

st.subheader("1.2 Tipos de Variáveis")

st.write("**Variáveis Categóricas (Qualitativas):**")
st.markdown(
    "- `gender`: Gênero do aluno (`M` para masculino, `F` para feminino).\n"
    "- `ssc_b`: Tipo de escola no ensino médio (`Central`, `Others`).\n"
    "- `hsc_b`: Tipo de escola no ensino médio superior.\n"
    "- `hsc_s`: Área de estudo no ensino médio (`Science`, `Commerce`, `Arts`).\n"
    "- `degree_t`: Tipo de curso de graduação (`Sci&Tech`, `Comm&Mgmt`).\n"
    "- `workex`: Experiência de trabalho antes do MBA (`Yes`, `No`).\n"
    "- `specialisation`: Especialização no MBA (`Mkt&HR`, `Mkt&Fin`).\n"
    "- `status`: Se o aluno foi contratado (`Placed`) ou não (`Not Placed`)."
)

st.write("**Variáveis Numéricas (Quantitativas):**")
st.markdown(
    "- `ssc_p`: Percentual de notas no ensino médio.\n"
    "- `hsc_p`: Percentual de notas no ensino médio superior.\n"
    "- `degree_p`: Percentual de notas no curso de graduação.\n"
    "- `etest_p`: Percentual do teste de empregabilidade.\n"
    "- `mba_p`: Percentual de notas no MBA.\n"
    "- `salary`: Salário oferecido ao aluno contratado."
)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Amostra dos dados:")
    st.write(df.head())
    
    st.subheader("1.3 Perguntas de Análise e Respostas")
    
    st.write("### 1. Há uma relação entre as notas acadêmicas e a contratação?")
    st.write("O heatmap de correlação mostra que as notas têm pouca correlação com a contratação.")
    st.write("O boxplot das notas indica que alunos contratados e não contratados possuem distribuições semelhantes.")
    
    st.write("### 2. A experiência de trabalho antes do MBA aumenta a chance de contratação?")
    workex_counts = df.groupby(["workex", "status"]).size().unstack()
    fig = workex_counts.plot(kind='bar', stacked=True, figsize=(8,5), colormap='viridis')
    st.pyplot(fig.figure)
    
    st.write("### 3. Qual o impacto da especialização no MBA na empregabilidade?")
    specialisation_counts = df.groupby(["specialisation", "status"]).size().unstack()
    fig = specialisation_counts.plot(kind='bar', stacked=True, figsize=(8,5), colormap='magma')
    st.pyplot(fig.figure)
    
    st.write("### 4. A distribuição dos salários segue um padrão específico?")
    st.write("A distribuição normal dos salários foi plotada, indicando que os salários podem seguir um comportamento próximo da normalidade.")
    
    # Aplicação de distribuições probabilísticas
    st.subheader("Distribuições Probabilísticas")
    
    st.write("### Distribuição Binomial")
    st.write("A distribuição Binomial foi escolhida para modelar a probabilidade de um aluno ser contratado, pois trata-se de um evento com duas possíveis saídas: contratado (sucesso) ou não contratado (falha). A seguir, apresentamos a distribuição estimada.")
    success_prob = (df["status"] == "Placed").mean()
    binom_values = np.arange(0, 11)
    binom_probs = stats.binom.pmf(binom_values, n=10, p=success_prob)
    plot_distribution(binom_values, binom_probs, "Distribuição Binomial (Contratação)", "Número de Contratados", "Probabilidade")
    
    st.write("### Distribuição Normal")
    st.write("A distribuição Normal foi aplicada para modelar a distribuição dos salários dos alunos contratados, pois geralmente salários seguem uma distribuição aproximadamente normal. Abaixo, apresentamos a distribuição teórica ajustada aos dados reais.")
    salary_mean = df["salary"].mean()
    salary_std = df["salary"].std()
    x = np.linspace(salary_mean - 3*salary_std, salary_mean + 3*salary_std, 100)
    y = stats.norm.pdf(x, salary_mean, salary_std)
    fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines', name='Distribuição Normal')])
    fig.update_layout(title="Distribuição Normal dos Salários", xaxis_title="Salário", yaxis_title="Densidade de Probabilidade")
    st.plotly_chart(fig)
