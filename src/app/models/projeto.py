class Projeto:
    _contador_id = 0

    def __init__(self, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao

        # Incrementa o contador de IDs para o próximo projeto
        Projeto._contador_id += 1

        self.id = Projeto._contador_id
    
    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Descrição: {self.descricao}"