import os

tarefas = [{'nome':'Estudar'}, 
           {'nome':'Treinar'}, 
           {'nome':'Acordar cedo'}]

def nome_do_app():
    print("""
██╗░░░░░██╗░██████╗████████╗░█████╗░  ██████╗░███████╗
██║░░░░░██║██╔════╝╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝
██║░░░░░██║╚█████╗░░░░██║░░░███████║  ██║░░██║█████╗░░
██║░░░░░██║░╚═══██╗░░░██║░░░██╔══██║  ██║░░██║██╔══╝░░
███████╗██║██████╔╝░░░██║░░░██║░░██║  ██████╔╝███████╗
╚══════╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝  ╚═════╝░╚══════╝

████████╗░█████╗░██████╗░███████╗███████╗░█████╗░░██████╗
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝
░░░██║░░░███████║██████╔╝█████╗░░█████╗░░███████║╚█████╗░
░░░██║░░░██╔══██║██╔══██╗██╔══╝░░██╔══╝░░██╔══██║░╚═══██╗
░░░██║░░░██║░░██║██║░░██║███████╗██║░░░░░██║░░██║██████╔╝
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░

""")

def opcoes():
    print('1. Adicionar Tarefa.')
    print('2. Listar Tarefas.')
    print('3. Remover Tarefa.')
    print('4. Sair.\n')

def opcao_escolhida():
    
    try:
        opcao_escolhida = int(input('Selecione uma opção: '))

        if opcao_escolhida == 1:
            adicionar_tarefa()
        elif opcao_escolhida == 2:
            listar_tarefas()
        elif opcao_escolhida == 3:
            remover_tarefa()
        elif opcao_escolhida == 4:
            finalizar_app()
        else: 
            opcao_invalida()
            
    except ValueError:
        opcao_invalida()

def adicionar_tarefa():
    os.system('cls')
    print('\nAdicionar Tarefa\n')

    nome_tarefa = input('Digite o nome da tarefa que deseja adicionar: ')
    tarefas.append({'nome':nome_tarefa})
    print(f'\nTarefa {nome_tarefa} adicionada com sucesso.\n')
    input('Aperte qualquer botão para retornar ao menu principal. ')
    main()


def listar_tarefas():
    os.system('cls')
    print('\nLista de Tarefas\n')

    for tarefa in tarefas:
        print(f'- {tarefa['nome']}')

    print('\nEssas são todas as tarefas registradas.\n')
    input('Aperte qualquer botão para retornar ao menu principal. ')
    main()

def remover_tarefa():
    os.system('cls')
    print('\nRemover Tarefa\n')
    
    nome_tarefa = input('Digite o nome da tarefa que deseja remover: ')
    tarefa_encontrada = False

    for tarefa in tarefas:
        if nome_tarefa == tarefa['nome']:
            tarefa_encontrada = True
            tarefas.remove(tarefa)
            print(f'\nTarefa {nome_tarefa} removida com sucesso.\n')
            break
            
    if not tarefa_encontrada:
        print('\nTarefa não encontrada\n')

    input('Aperte qualquer botão para retornar ao menu principal. ')
    main()

def finalizar_app():
    os.system('cls')
    print('Finalizando o app...\n')

def opcao_invalida():
    print('\nOpção Inválida\n')
    input('Aperte qualquer botão para retornar ao menu principal. ')
    main()


def main():
    os.system('cls')
    nome_do_app()
    opcoes()
    opcao_escolhida()

if __name__ == '__main__':
    main()