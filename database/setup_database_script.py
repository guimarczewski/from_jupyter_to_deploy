from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

import os
import sys
from dotenv import load_dotenv

# carregar variaveis de ambiente
load_dotenv()

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

# Seu modelo de dados
Base = declarative_base()

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Float, nullable=False)

# Seus dados
produtos_data = [
    {"id": 1, "titulo": "Cadeira Gamer", "descricao": "Cadeira confortável para fazer live", "preco": 1200.00},
    {"id": 2, "titulo": "Iphone", "descricao": "Iphone 14", "preco": 2500.00},
    {"id": 3, "titulo": "Iphone", "descricao": "Iphone 14", "preco": 2500.00},
    {"id": 4, "titulo": "Notebook Dell", "descricao": "Notebook para trabalho e estudo", "preco": 3000.00},
    {"id": 5, "titulo": "Smart TV 4K", "descricao": "TV com resolução 4K para uma experiência incrível", "preco": 2000.00},
    {"id": 6, "titulo": "Fones de Ouvido Bluetooth", "descricao": "Fones sem fio para uma experiência auditiva livre", "preco": 150.00},
    {"id": 7, "titulo": "Console de Videogame", "descricao": "Console para jogos de última geração", "preco": 500.00},
    {"id": 8, "titulo": "Máquina de Café Automática", "descricao": "Prepara café delicioso com um toque", "preco": 400.00},
    {"id": 9, "titulo": "Monitor UltraWide", "descricao": "Monitor expansivo para multitarefa eficiente", "preco": 600.00},
    {"id": 10, "titulo": "Mouse Gamer", "descricao": "Mouse com sensor de alta precisão para jogos", "preco": 80.00},
    {"id": 11, "titulo": "Teclado Mecânico RGB", "descricao": "Teclado mecânico com iluminação personalizável", "preco": 120.00},
    {"id": 12, "titulo": "Aspirador de Pó Robô", "descricao": "Aspirador automático para facilitar a limpeza", "preco": 250.00},
    {"id": 13, "titulo": "Caixa de Som Bluetooth", "descricao": "Caixa de som portátil para ouvir sua música favorita", "preco": 100.00},
    {"id": 14, "titulo": "Impressora Multifuncional", "descricao": "Impressora que imprime, copia e digitaliza", "preco": 150.00},
    {"id": 15, "titulo": "HD Externo 1TB", "descricao": "Armazenamento externo para backup e transporte de dados", "preco": 80.00},
    {"id": 16, "titulo": "Câmera DSLR", "descricao": "Câmera profissional para capturar momentos especiais", "preco": 1200.00},
    {"id": 17, "titulo": "Mesa de Escritório", "descricao": "Mesa espaçosa para um ambiente de trabalho confortável", "preco": 300.00},
    {"id": 18, "titulo": "Bicicleta Ergométrica", "descricao": "Bicicleta para exercícios físicos em casa", "preco": 400.00},
    {"id": 19, "titulo": "Secador de Cabelo Profissional", "descricao": "Secador potente para cuidados com o cabelo", "preco": 50.00},
    {"id": 20, "titulo": "Mala de Viagem", "descricao": "Mala resistente e espaçosa para suas viagens", "preco": 70.00},
    {"id": 21, "titulo": "Relógio Inteligente", "descricao": "Relógio com funções inteligentes e monitoramento de saúde", "preco": 200.00},
    {"id": 22, "titulo": "Ventilador de Torre", "descricao": "Ventilador compacto para refrescar o ambiente", "preco": 60.00},
    {"id": 23, "titulo": "Smartphone Android", "descricao": "Smartphone com sistema operacional Android", "preco": 800.00},
    {"id": 24, "titulo": "Cadeira Ergonômica", "descricao": "Cadeira projetada para proporcionar conforto e suporte", "preco": 350.00},
    {"id": 25, "titulo": "Cafeteira Programável", "descricao": "Cafeteira com programação para preparar café automaticamente", "preco": 120.00},
    {"id": 26, "titulo": "Tablet 10 polegadas", "descricao": "Tablet para entretenimento e produtividade", "preco": 300.00},
    {"id": 27, "titulo": "Luminária de Mesa LED", "descricao": "Luminária com iluminação LED ajustável", "preco": 40.00},
    {"id": 28, "titulo": "HD SSD 500GB", "descricao": "Armazenamento SSD para alta velocidade de leitura e gravação", "preco": 100.00},
    {"id": 29, "titulo": "Churrasqueira Elétrica", "descricao": "Churrasqueira para uso interno com controle de temperatura", "preco": 180.00},
    {"id": 30, "titulo": "Máquina de Lavar Roupa", "descricao": "Máquina com múltiplos programas de lavagem", "preco": 600.00},
    {"id": 31, "titulo": "Tênis Esportivo", "descricao": "Tênis confortável para prática de esportes", "preco": 80.00},
    {"id": 32, "titulo": "Fogão a Gás", "descricao": "Fogão com queimadores a gás para cozimento rápido", "preco": 400.00},
    {"id": 33, "titulo": "Caixa de Ferramentas", "descricao": "Caixa organizadora com diversas ferramentas", "preco": 50.00},
    {"id": 34, "titulo": "Mochila para Laptop", "descricao": "Mochila resistente com compartimento acolchoado para laptop", "preco": 60.00},
    {"id": 35, "titulo": "Panela Elétrica de Arroz", "descricao": "Panela elétrica para preparar arroz de forma prática", "preco": 45.00},
    {"id": 36, "titulo": "Laptop Ultrafino", "descricao": "Laptop leve e portátil para uso diário", "preco": 900.00},
    {"id": 37, "titulo": "Mini Geladeira", "descricao": "Geladeira compacta para bebidas e snacks", "preco": 120.00},
    {"id": 38, "titulo": "Batedeira Planetária", "descricao": "Batedeira com múltiplas velocidades para preparo de receitas", "preco": 80.00},
    {"id": 39, "titulo": "Fraldas Descartáveis", "descricao": "Pacote de fraldas para bebês", "preco": 30.00},
    {"id": 40, "titulo": "Micro-ondas Digital", "descricao": "Micro-ondas com funções programáveis", "preco": 150.00},
    {"id": 41, "titulo": "Cadeado Eletrônico", "descricao": "Cadeado com controle eletrônico para segurança", "preco": 23.00},
    {"id": 42, "titulo": "Tapete Antiderrapante", "descricao": "Tapete para prevenir escorregões em áreas úmidas", "preco": 25.00}
]

# Conectar ao banco de dados
DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(DATABASE_URL)

# Criar uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Criação da tabela no banco de dados
Base.metadata.create_all(bind=engine)

# Inserir dados na tabela
for produto_data in produtos_data:
    produto = Produto(**produto_data)
    session.add(produto)

# Commit das mudanças
session.commit()

# Fechar a sessão
session.close()

# Encerrar docker container
sys.exit()