class Usuario:
    _contador_id = 0

    def __init__(self, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

        Usuario._contador_id += 1

        self.id = Usuario._contador_id
    
    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | E-mail: {self.email}"
    
    def __repr__(self):
        """
        Representação "oficial" do objeto (para debugging)
        """
        return f"Usuario(ID: {self.id}, Nome: '{self.nome}', Email: '{self.email}')"
