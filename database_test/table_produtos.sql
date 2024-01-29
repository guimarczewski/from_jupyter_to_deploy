CREATE DATABASE sales;

\c sales;

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT,
    preco NUMERIC(10,2)
);