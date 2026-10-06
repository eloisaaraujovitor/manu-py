import streamlit as st
import pandas as pd
import numpy as np

# 1. Configuração da página no navegador
st.set_page_config(
    page_title="Meu Painel Streamlit",
    page_icon="🚀",
    layout="centered"
)

# 2. Título e cabeçalho
st.title("🚀 Meu Primeiro App com Streamlit")
st.write("Este é um painel interativo rodando direto do seu código Python!")

st.divider()

# 3. Entrada de dados pelo usuário
st.header("👤 Formulário do Usuário")

nome = st.text_input("Qual é o seu nome?", placeholder="Digite seu nome aqui...")
idade = st.slider("Selecione sua idade:", min_value=1, max_value=100, value=25)
linguagem = st.selectbox(
    "Qual sua linguagem de programação favorita?",
    ["Python", "JavaScript", "C++", "Java", "Outra"]
)

# Botão de envio
if st.button("Enviar Dados"):
    st.success(f"Olá **{nome if nome else 'Dev'}**! Cadastro realizado com sucesso.")
    st.info(f"Idade: {idade} anos | Linguagem Favorita: {linguagem}")

st.divider()

# 4. Exibição de Dados e Gráfico
st.header("📊 Dados e Gráficos Interativos")

st.write("Abaixo está um gráfico gerado automaticamente com dados aleatórios:")

# Gerando dados de exemplo
dados_grafico = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Vendas', 'Acessos', 'Lucro']
)

# Exibindo tabela expansível
with st.expander("Clique para ver a tabela de dados bruta"):
    st.dataframe(dados_grafico)

# Exibindo gráfico de linha
st.line_chart(dados_grafico)