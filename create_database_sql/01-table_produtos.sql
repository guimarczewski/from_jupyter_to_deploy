-- Aguarde 10 segundos para garantir que o PostgreSQL tenha iniciado completamente
SELECT pg_sleep(15);

CREATE DATABASE sales;

\c sales;

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT,
    preco NUMERIC(10,2)
);