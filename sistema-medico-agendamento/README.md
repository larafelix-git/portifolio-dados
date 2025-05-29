# Sistema Médico de Agendamento

Este projeto é uma aplicação web simples para gerenciamento de agendamentos médicos, desenvolvida com **Python** e **Flask** **MySQL**.

## Funcionalidades principais

- Cadastro e visualização de agendamentos médicos.
- Interface web com formulários para inclusão e consulta dos dados.
- Utilização de banco de dados para armazenamento dos agendamentos (MySQL).
- Estrutura organizada com templates HTML para as páginas.
- Sistema básico para facilitar o gerenciamento de horários em uma clínica odontológica ou médica.
- É possível consultar os agendamentos, criei essa funcionalidade pois o GitHub não tem suporte a Banco de Dados.

## Tecnologias usadas

- Python 3
- Flask
- MySQL
- HTML (templates) & CSS

## Script Usado no Banco de Dados MySQL Workbench

DROP TABLE IF EXISTS Agendamento;
DROP TABLE IF EXISTS Emergencia;
DROP TABLE IF EXISTS Medico;
DROP TABLE IF EXISTS Clinica;
DROP TABLE IF EXISTS Medicamento;
DROP TABLE IF EXISTS Tutor;

CREATE TABLE Tutor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    contato VARCHAR(20)
);

CREATE TABLE Medicamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    descricao TEXT
);

CREATE TABLE Clinica (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    endereco TEXT
);

CREATE TABLE Medico (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    crm VARCHAR(20),
    contato VARCHAR(20)
);

CREATE TABLE Emergencia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    contato VARCHAR(20)
);

CREATE TABLE Agendamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao_alerta TEXT,
    data_agendamento DATE,
    hora_agendamento TIME,
    tutor_id INT,
    medicamento_id INT,
    clinica_id INT,
    medico_id INT,
    emergencia1_id INT,
    emergencia2_id INT,
    FOREIGN KEY (tutor_id) REFERENCES Tutor(id),
    FOREIGN KEY (medicamento_id) REFERENCES Medicamento(id),
    FOREIGN KEY (clinica_id) REFERENCES Clinica(id),
    FOREIGN KEY (medico_id) REFERENCES Medico(id),
    FOREIGN KEY (emergencia1_id) REFERENCES Emergencia(id),
    FOREIGN KEY (emergencia2_id) REFERENCES Emergencia(id)
);

## Instalação
1. Clone este repositório:
bash
git clone https://github.com/larafelix-git/portifolio-dados.git

2. Navegue até a pasta do projeto:
bash
cd portifolio-dados/sistema-medico-agendamento

3. Configure o banco de dados MySQL:
Importe o script SQL disponível acima no MySQL Workbench ou em outro cliente MySQL para criar as tabelas necessárias.

Configure a conexão com o banco de dados no arquivo db.py ajustando as credenciais conforme seu ambiente local:

db.py
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sua_senha_aqui",
        database="sistema_medico_agendamentos"
    )
4. Vá na pasta app.py e coloque o projeto para rodar
bash
py app.py
clique no link gerado 

