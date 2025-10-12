from src.app.models.usuario import Usuario

# "Banco de dados" em memória
_lista_de_usuarios = []

def _encontrar_usuario_por_id(id_usuario: int):
    """
    Função auxiliar para encontrar um usuário na lista pelo seu ID.
    Retorna o objeto Usuario se encontrado, ou None caso contrário.
    """
    for usuario in _lista_de_usuarios:
        if usuario.id == id_usuario:
            return usuario
    return None

def cadastrar_novo_usuario():
    """Solicita os dados ao usuário, cria uma instância e a salva."""
    print("\n--- Cadastro de Novo Usuário ---")
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")

    if not nome or not email:
        print("\n[ERRO] Nome e email não podem ser vazios!")
        return

    for u in _lista_de_usuarios:
        if u.email == email:
            print(f"\n[ERRO] O email '{email}' já está cadastrado!")
            return

    novo_usuario = Usuario(nome=nome, email=email)
    _lista_de_usuarios.append(novo_usuario)
    print(f"\n[SUCESSO] Usuário '{novo_usuario.nome}' (ID: {novo_usuario.id}) cadastrado com sucesso!")

def listar_usuarios():
    """Lista todos os usuários cadastrados."""
    print("\n--- Lista de Usuários Cadastrados ---")
    if not _lista_de_usuarios:
        print("Nenhum usuário cadastrado no sistema.")
        return 0
    for usuario in _lista_de_usuarios:
        print(usuario)
    print("---------------------------------------")
    return _lista_de_usuarios.copy()

# --- NOVAS FUNÇÕES ABAIXO ---

def atualizar_usuario():
    """
    Solicita o ID de um usuário, busca por ele e atualiza seus dados.
    """
    print("\n--- Atualização de Usuário ---")
    listar_usuarios() # Mostra os usuários para facilitar a escolha
    
    try:
        id_para_atualizar = int(input("Digite o ID do usuário que deseja atualizar: "))
    except ValueError:
        print("\n[ERRO] ID inválido. Por favor, digite um número.")
        return

    usuario_encontrado = _encontrar_usuario_por_id(id_para_atualizar)

    if not usuario_encontrado:
        print(f"\n[ERRO] Usuário com ID {id_para_atualizar} não encontrado.")
        return

    print(f"Atualizando dados para: {usuario_encontrado.nome}")
    novo_nome = input(f"Digite o novo nome (ou pressione Enter para manter '{usuario_encontrado.nome}'): ")
    novo_email = input(f"Digite o novo email (ou pressione Enter para manter '{usuario_encontrado.email}'): ")

    # Lógica para atualizar os campos apenas se algo foi digitado
    if novo_nome:
        usuario_encontrado.nome = novo_nome
    if novo_email:
        # Seria bom adicionar uma verificação de email duplicado aqui também
        usuario_encontrado.email = novo_email
    
    print(f"\n[SUCESSO] Usuário atualizado: {usuario_encontrado}")

def deletar_usuario():
    """
    Solicita o ID de um usuário e o remove da lista.
    """
    print("\n--- Deletar Usuário ---")
    listar_usuarios() # Mostra os usuários para facilitar a escolha

    try:
        id_para_deletar = int(input("Digite o ID do usuário que deseja deletar: "))
    except ValueError:
        print("\n[ERRO] ID inválido. Por favor, digite um número.")
        return
        
    usuario_encontrado = _encontrar_usuario_por_id(id_para_deletar)

    if not usuario_encontrado:
        print(f"\n[ERRO] Usuário com ID {id_para_deletar} não encontrado.")
        return

    # Confirmação antes de deletar
    confirmacao = input(f"Tem certeza que deseja deletar o usuário '{usuario_encontrado.nome}'? (s/n): ").lower()

    if confirmacao == 's':
        _lista_de_usuarios.remove(usuario_encontrado)
        print(f"\n[SUCESSO] Usuário '{usuario_encontrado.nome}' foi deletado.")
    else:
        print("\nOperação de deleção cancelada.")