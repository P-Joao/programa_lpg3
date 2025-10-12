from src.app.services.servico_usuario import cadastrar_novo_usuario, listar_usuarios, atualizar_usuario, deletar_usuario

def exibir_menu_usuario():
    """Mostra as opções do menu para o usuário."""
    print("\n--- Menu de Usuários ---")
    print("1: Cadastrar Usuário")
    print("2: Lista Usuários")
    print("3: Atualizar Usuário")
    print("4: Apagar Usuário")
    print("0: Voltar")
    print("--------------------------------")

def iniciar_menu_usuario():
    """Inicia o loop principal da aplicação CLI."""
    while True:
        exibir_menu_usuario()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n[INFO] Opção 'Cadastrar Usuário' selecionada.")
            cadastrar_novo_usuario()

        elif opcao == '2':
            print("\n[INFO] Opção 'Listar Usuários' selecionada.")
            listar_usuarios()
        
        elif opcao == '3':
            print("\n[INFO] Opção 'Atualizar Usuário' selecionada.")
            atualizar_usuario()

        elif opcao == '4':
            print("\n[INFO] Opção 'Deletar Usuário' selecionada.")
            deletar_usuario()

        elif opcao == '0':
            break
        else:
            print("\n[ERRO] Opção inválida. Tente novamente.")