from src.app.models.tarefa import Tarefa

from src.app.services.servico_projeto import listar_projetos
from src.app.services.servico_categoria import listar_categorias
from src.app.services.servico_usuario import listar_usuarios

# "Banco de dados" em memória
_lista_de_tarefas = []

def _encontrar_tarefa_por_id(id_tarefa: int):
    """
    Função auxiliar para encontrar uma tarefa na lista pelo seu ID.
    Retorna o objeto Tarefa se encontrado, ou None caso contrário.
    """
    for tarefa in _lista_de_tarefas:
        if tarefa.id == id_tarefa:
            return tarefa
    return None

def _encontrar_outro_por_id(lista_outro: list, id_outro: int):
    """
    Função auxiliar para encontrar uma tarefa na lista pelo seu ID.
    Retorna o objeto Tarefa se encontrado, ou None caso contrário.
    """
    for outro in lista_outro:
        if outro.id == id_outro:
            return outro
    return None

def cadastrar_nova_tarefa():
    """Solicita os dados ao usuário, cria uma instância e a salva."""
    print("\n--- Cadastro de Nova Tarefa ---")
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")

    if not titulo or not descricao:
        print("\n[ERRO] Título e descrição não podem ser vazios!")
        return
    for t in _lista_de_tarefas:
        if t.titulo == titulo:
            print(f"\n[ERRO] A tarefa '{titulo}' já está cadastrada!")
            return

    # Associar tarefa a um projeto existente
    projetos = listar_projetos()
    projeto_id = input("Digite o ID do projeto que deseja associar a tarefa: ")
    projeto = _encontrar_outro_por_id(projetos, int(projeto_id))
    if not projeto:
        print(f"\n[ERRO] Projeto com ID {projeto_id} não encontrado.")
        return
    print(f"Projeto selecionado: {projeto.nome}")
    
    #Associar tarefa a um usuário existente
    usuarios = listar_usuarios()
    usuario_id = input("Digite o ID do usuário que deseja associar a tarefa: ")
    usuario = _encontrar_outro_por_id(usuarios, int(usuario_id))
    if not usuario:
        print(f"\n[ERRO] Usuário com ID {usuario_id} não encontrado.")
        return
    print(f"Usuário selecionado: {usuario.nome}")
    
    #Associar tarefa a uma categoria existente
    categorias = listar_categorias()
    categoria_id = input("Digite o ID da categoria que deseja associar a tarefa: ")
    categoria = _encontrar_outro_por_id(categorias, int(categoria_id))
    if not categoria:
        print(f"\n[ERRO] Categoria com ID {categoria_id} não encontrada.")
        return
    print(f"Categoria selecionada: {categoria.nome}")

    prioridade = input("Digite a prioridade da tarefa (Baixa, Média, Alta): ")
    status = input("Digite o status da tarefa (Pendente, Em Progresso, Concluída): ")
    prazo = input("Digite o prazo da tarefa (formato YYYY-MM-DD): ")

    nova_tarefa = Tarefa(titulo=titulo, descricao=descricao, projeto_id=projeto.id, responsavel_id=usuario.id, categoria_id=categoria.id, prioridade=prioridade, status=status, prazo=prazo)
    _lista_de_tarefas.append(nova_tarefa)
    print(f"\n[SUCESSO] Tarefa '{nova_tarefa.titulo}' (ID: {nova_tarefa.id}) cadastrada com sucesso!")

def listar_tarefas():
    """Lista todas as tarefas cadastradas."""
    print("\n--- Lista de Tarefas Cadastrados ---")
    if not _lista_de_tarefas:
        print("Nenhuma tarefa cadastrada no sistema.")
        return
    for tarefa in _lista_de_tarefas:
        print(tarefa)
    print("---------------------------------------")

# --- NOVAS FUNÇÕES ABAIXO ---

def atualizar_tarefa():
    """
    Solicita o ID de uma tarefa, busca por ela e atualiza seus dados.
    """
    print("\n--- Atualização de Tarefa ---")
    listar_tarefas() # Mostra as tarefas para facilitar a escolha
    
    try:
        id_para_atualizar = int(input("Digite o ID da tarefa que deseja atualizar: "))
    except ValueError:
        print("\n[ERRO] ID inválido. Por favor, digite um número.")
        return

    tarefa_encontrada = _encontrar_tarefa_por_id(id_para_atualizar)

    if not tarefa_encontrada:
        print(f"\n[ERRO] Tarefa com ID {id_para_atualizar} não encontrada.")
        return

    print(f"Atualizando dados para: {tarefa_encontrada.titulo}")
    nova_descricao = input(f"Digite a nova descrição (ou pressione Enter para manter '{tarefa_encontrada.descricao}'): ")
    nova_prioridade = input(f"Digite a nova prioridade (ou pressione Enter para manter '{tarefa_encontrada.prioridade}'): ")

    # Lógica para atualizar os campos apenas se algo foi digitado
    if nova_descricao:
        tarefa_encontrada.descricao = nova_descricao
    if nova_prioridade:
        # Seria bom adicionar uma verificação de prioridade duplicada aqui também
        tarefa_encontrada.prioridade = nova_prioridade

    print("Deseja atualizar o status da tarefa? (s/n)")
    if input().lower() == 's':
        novo_status = input(f"Digite o novo status (ou pressione Enter para manter '{tarefa_encontrada.status}'): ")
        if novo_status:
            tarefa_encontrada.status = novo_status
    
    print("Deseja atualizar o prazo da tarefa? (s/n)")
    if input().lower() == 's':
        novo_prazo = input(f"Digite o novo prazo (ou pressione Enter para manter '{tarefa_encontrada.prazo}'): ")
        if novo_prazo:
            tarefa_encontrada.prazo = novo_prazo

    print("Deseja atualizar o projeto associado? (s/n)")
    if input().lower() == 's':
        projetos = listar_projetos()
        novo_projeto_id = input("Digite o ID do novo projeto: ")
        novo_projeto = _encontrar_outro_por_id(projetos, int(novo_projeto_id))
        if novo_projeto:
            tarefa_encontrada.projeto = novo_projeto
        else:
            print(f"\n[ERRO] Projeto com ID {novo_projeto_id} não encontrado. Mantendo o projeto atual.")
    
    print("Deseja atualizar o usuário responsável? (s/n)")
    if input().lower() == 's':
        usuarios = listar_usuarios()
        novo_usuario_id = input("Digite o ID do novo usuário: ")
        novo_usuario = _encontrar_outro_por_id(usuarios, int(novo_usuario_id))
        if novo_usuario:
            tarefa_encontrada.usuario = novo_usuario
        else:
            print(f"\n[ERRO] Usuário com ID {novo_usuario_id} não encontrado. Mantendo o usuário atual.")
    
    print("Deseja atualizar a categoria associada? (s/n)")
    if input().lower() == 's':
        categorias = listar_categorias()
        nova_categoria_id = input("Digite o ID da nova categoria: ")
        nova_categoria = _encontrar_outro_por_id(categorias, int(nova_categoria_id))
        if nova_categoria:
            tarefa_encontrada.categoria = nova_categoria
        else:
            print(f"\n[ERRO] Categoria com ID {nova_categoria_id} não encontrada. Mantendo a categoria atual.")

    print(f"\n[SUCESSO] Tarefa atualizada: {tarefa_encontrada}")

def deletar_tarefa():
    """
    Solicita o ID de uma tarefa e a remove da lista.
    """
    print("\n--- Deletar Tarefa ---")
    listar_tarefas() # Mostra as tarefas para facilitar a escolha

    try:
        id_para_deletar = int(input("Digite o ID da tarefa que deseja deletar: "))
    except ValueError:
        print("\n[ERRO] ID inválido. Por favor, digite um número.")
        return
        
    tarefa_encontrada = _encontrar_tarefa_por_id(id_para_deletar)

    if not tarefa_encontrada:
        print(f"\n[ERRO] Tarefa com ID {id_para_deletar} não encontrada.")
        return

    # Confirmação antes de deletar
    confirmacao = input(f"Tem certeza que deseja deletar a tarefa '{tarefa_encontrada.titulo}'? (s/n): ").lower()

    if confirmacao == 's':
        _lista_de_tarefas.remove(tarefa_encontrada)
        print(f"\n[SUCESSO] Tarefa '{tarefa_encontrada.titulo}' foi deletada.")
    else:
        print("\nOperação de deleção cancelada.")