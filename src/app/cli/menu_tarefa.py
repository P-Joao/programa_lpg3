from src.app.services.servico_tarefa import cadastrar_nova_tarefa, listar_tarefas, atualizar_tarefa, deletar_tarefa

def exibir_menu_tarefa():
    """Mostra as opções do menu para o projeto."""
    print("\n--- Menu de Tarefa ---")
    print("1: Cadastrar Tarefa")
    print("2: Listar Tarefas")
    print("3: Atualizar Tarefa")
    print("4: Deletar Tarefa")
    print("0: Voltar")
    print("--------------------------------")

def iniciar_menu_tarefa():
    """Inicia o loop principal da aplicação CLI."""
    while True:
        exibir_menu_tarefa()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n[INFO] Opção 'Cadastrar Tarefa' selecionada.")
            cadastrar_nova_tarefa()

        elif opcao == '2':
            print("\n[INFO] Opção 'Listar Tarefas' selecionada.")
            listar_tarefas()

        elif opcao == '3':
            print("\n[INFO] Opção 'Atualizar Tarefa' selecionada.")
            atualizar_tarefa()

        elif opcao == '4':
            print("\n[INFO] Opção 'Deletar Tarefa' selecionada.")
            deletar_tarefa()

        elif opcao == '0':
            break
        else:
            print("\n[ERRO] Opção inválida. Tente novamente.")