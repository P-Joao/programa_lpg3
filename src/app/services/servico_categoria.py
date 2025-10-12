from src.app.models.categoria import Categoria

# "Banco de dados" em memória
_lista_de_categorias = []

def _encontrar_categoria_por_id(id_categoria: int):
    """
    Função auxiliar para encontrar uma categoria na lista pelo seu ID.
    Retorna o objeto Categoria se encontrado, ou None caso contrário.
    """
    for categoria in _lista_de_categorias:
        if categoria.id == id_categoria:
            return categoria
    return None

def cadastrar_nova_categoria():
    """Solicita os dados ao usuário, cria uma instância e a salva."""
    print("\n--- Cadastro de Nova Categoria ---")
    nome = input("Digite o nome da categoria: ")

    if not nome:
        print("\n[ERRO] Nome não pode ser vazio!")
        return

    for c in _lista_de_categorias:
        if c.nome == nome:
            print(f"\n[ERRO] A categoria '{nome}' já está cadastrada!")
            return

    nova_categoria = Categoria(nome=nome)
    _lista_de_categorias.append(nova_categoria)
    print(f"\n[SUCESSO] Categoria '{nova_categoria.nome}' (ID: {nova_categoria.id}) cadastrada com sucesso!")
    print("Para adicionar tarefas ao projeto, utilize a opção de 'Menu de Tarefas' no menu principal.")

def listar_categorias():
    """Lista todas as categorias cadastradas."""
    print("\n--- Lista de Categorias Cadastradas ---")
    if not _lista_de_categorias:
        print("Nenhuma categoria cadastrada no sistema.")
        return 0
    for categoria in _lista_de_categorias:
        print(categoria)
    print("---------------------------------------")
    return _lista_de_categorias.copy()

# --- NOVAS FUNÇÕES ABAIXO ---

def atualizar_categoria():
    """
    Solicita o ID de uma categoria, busca por ela e atualiza seus dados.
    """
    print("\n--- Atualização de Categoria ---")
    listar_categorias() # Mostra as categorias para facilitar a escolha
    
    try:
        id_para_atualizar = int(input("Digite o ID da categoria que deseja atualizar: "))
    except ValueError:
        print("\n[ERRO] ID inválido. Por favor, digite um número.")
        return

    categoria_encontrada = _encontrar_categoria_por_id(id_para_atualizar)

    if not categoria_encontrada:
        print(f"\n[ERRO] Categoria com ID {id_para_atualizar} não encontrada.")
        return

    print(f"Atualizando dados para: {categoria_encontrada.nome}")
    novo_nome = input(f"Digite o novo nome (ou pressione Enter para manter '{categoria_encontrada.nome}'): ")
    for c in _lista_de_categorias:
        if c.nome == novo_nome:
            print(f"\n[ERRO] A categoria '{novo_nome}' já está cadastrada!")
            return

    # Lógica para atualizar os campos apenas se algo foi digitado
    if novo_nome:
        categoria_encontrada.nome = novo_nome

    print(f"\n[SUCESSO] Categoria atualizada: {categoria_encontrada}")

def deletar_categoria():
    """
    Solicita o ID de uma categoria e a remove da lista.
    """
    print("\n--- Deletar Categoria ---")
    listar_categorias()  # Mostra as categorias para facilitar a escolha

    try:
        id_para_deletar = int(input("Digite o ID da categoria que deseja deletar: "))
    except ValueError:
        print("\n[ERRO] ID inválido. Por favor, digite um número.")
        return

    categoria_encontrada = _encontrar_categoria_por_id(id_para_deletar)

    if not categoria_encontrada:
        print(f"\n[ERRO] Categoria com ID {id_para_deletar} não encontrada.")
        return

    # Confirmação antes de deletar
    confirmacao = input(f"Tem certeza que deseja deletar a categoria '{categoria_encontrada.nome}'? (s/n): ").lower()

    if confirmacao == 's':
        _lista_de_categorias.remove(categoria_encontrada)
        print(f"\n[SUCESSO] Categoria '{categoria_encontrada.nome}' foi deletada.")
    else:
        print("\nOperação de deleção cancelada.")