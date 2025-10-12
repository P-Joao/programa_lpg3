from src.app.services.servico_projeto import cadastrar_novo_projeto, listar_projetos, atualizar_projeto, deletar_projeto

def exibir_menu_projeto():
    """Mostra as opções do menu para o projeto."""
    print("\n--- Menu de Projetos ---")
    print("1: Cadastrar Projeto")
    print("2: Listar Projetos")
    print("3: Atualizar Projeto")
    print("4: Deletar Projeto")
    print("0: Voltar")
    print("--------------------------------")

def iniciar_menu_projeto():
    """Inicia o loop principal da aplicação CLI."""
    while True:
        exibir_menu_projeto()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n[INFO] Opção 'Cadastrar Projeto' selecionada.")
            cadastrar_novo_projeto()

        elif opcao == '2':
            print("\n[INFO] Opção 'Listar Projetos' selecionada.")
            listar_projetos()

        elif opcao == '3':
            print("\n[INFO] Opção 'Atualizar Projeto' selecionada.")
            atualizar_projeto()

        elif opcao == '4':
            print("\n[INFO] Opção 'Deletar Projeto' selecionada.")
            deletar_projeto()

        elif opcao == '0':
            break
        else:
            print("\n[ERRO] Opção inválida. Tente novamente.")