from src.app.services.servico_categoria import cadastrar_nova_categoria, listar_categorias, atualizar_categoria, deletar_categoria

def exibir_menu_categoria():
    """Mostra as opções do menu para a categoria."""
    print("\n--- Menu de Categorias ---")
    print("1: Cadastrar Categoria")
    print("2: Listar Categorias")
    print("3: Atualizar Categoria")
    print("4: Deletar Categoria")
    print("0: Voltar")
    print("--------------------------------")

def iniciar_menu_categoria():
    """Inicia o loop principal da aplicação CLI."""
    while True:
        exibir_menu_categoria()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n[INFO] Opção 'Cadastrar Categoria' selecionada.")
            cadastrar_nova_categoria()

        elif opcao == '2':
            print("\n[INFO] Opção 'Listar Categorias' selecionada.")
            listar_categorias()

        elif opcao == '3':
            print("\n[INFO] Opção 'Atualizar Categoria' selecionada.")
            atualizar_categoria()

        elif opcao == '4':
            print("\n[INFO] Opção 'Deletar Categoria' selecionada.")
            deletar_categoria()

        elif opcao == '0':
            break
        else:
            print("\n[ERRO] Opção inválida. Tente novamente.")