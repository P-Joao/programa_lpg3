from src.app.models.projeto import Projeto

# "Banco de dados" em memória
_lista_de_projetos = []

def _encontrar_projeto_por_id(id_projeto: int):
    """
    Função auxiliar para encontrar um projeto na lista pelo seu ID.
    Retorna o objeto Projeto se encontrado, ou None caso contrário.
    """
    for projeto in _lista_de_projetos:
        if projeto.id == id_projeto:
            return projeto
    return None

def cadastrar_novo_projeto():
    """Solicita os dados ao usuário, cria uma instância e a salva."""
    print("\n--- Cadastro de Novo Projeto ---")
    nome = input("Digite o nome do projeto: ")
    descricao = input("Digite a descrição do projeto: ")

    if not nome or not descricao:
        print("\n[ERRO] Nome e descrição não podem ser vazios!")
        return

    for p in _lista_de_projetos:
        if p.nome == nome:
            print(f"\n[ERRO] O projeto '{nome}' já está cadastrado!")
            return

    novo_projeto = Projeto(nome=nome, descricao=descricao)
    _lista_de_projetos.append(novo_projeto)
    print(f"\n[SUCESSO] Projeto '{novo_projeto.nome}' (ID: {novo_projeto.id}) cadastrado com sucesso!")
    print("Para adicionar tarefas ao projeto, utilize a opção de 'Menu de Tarefas' no menu principal.")

def listar_projetos():
    """Lista todos os projetos cadastrados."""
    print("\n--- Lista de Projetos Cadastrados ---")
    if not _lista_de_projetos:
        print("Nenhum projeto cadastrado no sistema.")
        return 0
    for projeto in _lista_de_projetos:
        print(projeto)
    print("---------------------------------------")
    return _lista_de_projetos.copy()

# --- NOVAS FUNÇÕES ABAIXO ---

def atualizar_projeto():
    """
    Solicita o ID de um projeto, busca por ele e atualiza seus dados.
    """
    print("\n--- Atualização de Projeto ---")
    listar_projetos() # Mostra os projetos para facilitar a escolha
    
    try:
        id_para_atualizar = int(input("Digite o ID do projeto que deseja atualizar: "))
    except ValueError:
        print("\n[ERRO] ID inválido. Por favor, digite um número.")
        return

    projeto_encontrado = _encontrar_projeto_por_id(id_para_atualizar)

    if not projeto_encontrado:
        print(f"\n[ERRO] Projeto com ID {id_para_atualizar} não encontrado.")
        return

    print(f"Atualizando dados para: {projeto_encontrado.nome}")
    novo_nome = input(f"Digite o novo nome (ou pressione Enter para manter '{projeto_encontrado.nome}'): ")
    novo_descricao = input(f"Digite a nova descrição (ou pressione Enter para manter '{projeto_encontrado.descricao}'): ")

    # Lógica para atualizar os campos apenas se algo foi digitado
    if novo_nome:
        projeto_encontrado.nome = novo_nome
    if novo_descricao:
        projeto_encontrado.descricao = novo_descricao

    print(f"\n[SUCESSO] Projeto atualizado: {projeto_encontrado}")

def deletar_projeto():
    """
    Solicita o ID de um projeto e o remove da lista.
    """
    print("\n--- Deletar Projeto ---")
    listar_projetos()  # Mostra os projetos para facilitar a escolha

    try:
        id_para_deletar = int(input("Digite o ID do projeto que deseja deletar: "))
    except ValueError:
        print("\n[ERRO] ID inválido. Por favor, digite um número.")
        return

    projeto_encontrado = _encontrar_projeto_por_id(id_para_deletar)

    if not projeto_encontrado:
        print(f"\n[ERRO] Projeto com ID {id_para_deletar} não encontrado.")
        return

    # Confirmação antes de deletar
    confirmacao = input(f"Tem certeza que deseja deletar o projeto '{projeto_encontrado.nome}'? (s/n): ").lower()

    if confirmacao == 's':
        _lista_de_projetos.remove(projeto_encontrado)
        print(f"\n[SUCESSO] Projeto '{projeto_encontrado.nome}' foi deletado.")
    else:
        print("\nOperação de deleção cancelada.")