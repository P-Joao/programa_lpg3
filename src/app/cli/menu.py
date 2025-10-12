from src.app.cli.menu_usuario import iniciar_menu_usuario, listar_usuarios
from src.app.cli.menu_projeto import iniciar_menu_projeto, listar_projetos
from src.app.cli.menu_categoria import iniciar_menu_categoria, listar_categorias
from src.app.cli.menu_tarefa import iniciar_menu_tarefa

def exibir_menu():
    """Mostra as opções do menu para o usuário."""
    print("\n--- Sistema de Gerenciamento ---")
    print("1: Menu de Usuários")
    print("2: Menu de Projetos")
    print("3: Menu de Categorias")
    print("4: Menu de Tarefas")
    print("0: Sair")
    print("--------------------------------")

def iniciar():
    """Inicia o loop principal da aplicação CLI."""
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n[INFO] Opção 'Menu de Usuários' selecionada.")
            iniciar_menu_usuario()

        elif opcao == '2':
            print("\n[INFO] Opção 'Menu de Projetos' selecionada.")
            iniciar_menu_projeto()
        
        elif opcao == '3':
            print("\n[INFO] Opção 'Menu de Categorias' selecionada.")
            iniciar_menu_categoria()

        elif opcao == '4':
            print("\n[INFO] Opção 'Menu de Tarefas' selecionada.")
            if listar_projetos() == 0:
                print("\n[ERRO] Nenhum projeto cadastrado. Cadastre um projeto antes de gerenciar tarefas.")
                continue
            if listar_categorias() == 0:
                print("\n[ERRO] Nenhuma categoria cadastrada. Cadastre uma categoria antes de gerenciar tarefas.")
                continue
            if listar_usuarios() == 0:
                print("\n[ERRO] Nenhum usuário cadastrado. Cadastre um usuário antes de gerenciar tarefas.")
                continue
            iniciar_menu_tarefa()

        elif opcao == '0':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("\n[ERRO] Opção inválida. Tente novamente.")