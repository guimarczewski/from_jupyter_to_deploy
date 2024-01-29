import streamlit as st

import pandas as pd

import os

from dotenv import load_dotenv

from sqlalchemy import create_engine

from plotly import graph_objects as go

# carregar variaveis de ambiente
load_dotenv()

db_password = os.getenv("POSTGRES_PASSWORD")
db_user = os.getenv("POSTGRES_USER")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

def connect_to_db():
    """
    Funcao para conectar ao banco de dados
    """
    engine = create_engine(
        f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    )
    return engine

def run_query(query,engine):
    with engine.connect() as conn:
        return pd.read_sql(query, conn)

def create_plot(df, plot_type):
    if plot_type == "bar":
        return go.Figure(data=[go.Bar(x=df["titulo"], y=df["preco"])])
    elif plot_type == "line":
        return go.Figure(
            data=[go.Scatter(x=df.index, y=df["preco"], mode="lines+markers")]
        )
    elif plot_type == "scatter":
        return go.Figure(
            data=[go.Scatter(x=df["titulo"], y=df["preco"], mode="markers")]
        )
    elif plot_type == "pie":
        return go.Figure(data=[go.Pie(labels=df["titulo"], values=df["preco"])])
    # Adicione outros tipos de gráficos conforme necessário

def main():
    st.title("Dashboard de Preços")

    engine = connect_to_db()
    query = "SELECT DISTINCT titulo, preco FROM produtos ORDER BY preco DESC"
    df = run_query(query, engine)

def main():
    st.title("Dashboard de Preços")

    engine = connect_to_db()
    query = "SELECT DISTINCT titulo, preco FROM produtos ORDER BY preco DESC"
    df = run_query(query, engine)

    st.write("Produtos:")
    st.dataframe(df)

    st.write("Top 5 Produtos (Atualizado):")
    st.dataframe(df)

    plot_types = ["bar", "line", "scatter", "pie"]
    plot_type = st.selectbox("Selecione o tipo de gráfico", plot_types)
    plot = create_plot(df, plot_type)
    st.plotly_chart(plot)

if __name__ == "__main__":
    main()