class Categoria:
    _contador_id = 0

    def __init__(self, nome):
        self.id = id
        self.nome = nome

        Categoria._contador_id += 1

        self.id = Categoria._contador_id
    
    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome}"