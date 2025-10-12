from datetime import datetime


class Tarefa:
    _contador_id = 0

    def __init__(self, titulo, descricao, projeto_id, responsavel_id, categoria_id, prioridade, status, prazo):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.projeto_id = projeto_id
        self.responsavel_id = responsavel_id
        self.categoria_id = categoria_id
        self.prioridade = prioridade
        self.status = status
        self.criacao = datetime.now()
        self.prazo = prazo

        Tarefa._contador_id += 1

        self.id = Tarefa._contador_id

    def __str__(self):
        return f"ID: {self.id} | Título: {self.titulo} | Descrição: {self.descricao} | projeto_id: {self.projeto_id} | responsavel_id: {self.responsavel_id} | categoria_id: {self.categoria_id} | Prioridade: {self.prioridade} | Status: {self.status} | Criacao: {self.criacao} | Prazo: {self.prazo}"