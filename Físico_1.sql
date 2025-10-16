/* Lógico_1: */

CREATE TABLE Usuario (
    id INTEGER PRIMARY KEY,
    nome VARCHAR,
    email VARCHAR
);

CREATE TABLE Categoria (
    id INTEGER PRIMARY KEY,
    nome VARCHAR
);

CREATE TABLE Projeto (
    id INTEGER PRIMARY KEY,
    nome VARCHAR,
    descricao VARCHAR
);

CREATE TABLE Tarefa (
    id INTEGER PRIMARY KEY,
    titulo VARCHAR,
    descricao VARCHAR,
    prioridade VARCHAR,
    prazo DATE,
    status VARCHAR,
    criacao DATE,
    fk_Usuario_id INTEGER,
    fk_Projeto_id INTEGER,
    fk_Categoria_id INTEGER
);
 
ALTER TABLE Tarefa ADD CONSTRAINT FK_Tarefa_2
    FOREIGN KEY (fk_Usuario_id)
    REFERENCES Usuario (id)
    ON DELETE CASCADE;
 
ALTER TABLE Tarefa ADD CONSTRAINT FK_Tarefa_3
    FOREIGN KEY (fk_Projeto_id)
    REFERENCES Projeto (id)
    ON DELETE CASCADE;
 
ALTER TABLE Tarefa ADD CONSTRAINT FK_Tarefa_4
    FOREIGN KEY (fk_Categoria_id)
    REFERENCES Categoria (id)
    ON DELETE CASCADE;