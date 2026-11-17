import os

tarefas = [{'nome':'Estudar'}, 
           {'nome':'Treinar'}, 
           {'nome':'Ler'}]

def nome_do_app():
    '''Exibe o nome do aplicativo.'''
    print('''
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

''')

def opcoes():
    '''Exibe as opções do menu.'''
    print('1. Adicionar Tarefa.')
    print('2. Listar Tarefas.')
    print('3. Remover Tarefa.')
    print('4. Sair.\n')

def opcao_escolhida():
    '''Lê a opção do usuário e chama a função correspondente.'''
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
    '''Pede o nome da tarefa ao usuário e a adiciona à lista de tarefas.'''
    exibir_subtitulo('Adicionar Tarefa')

    digitou_algo = False
    while not digitou_algo:
        nome_tarefa = input('Digite o nome da tarefa que deseja adicionar: ').strip()
        if nome_tarefa:
            digitou_algo = True
        else:
            exibir_subtitulo('Adicionar Tarefa')
            print('\nO nome da tarefa não pode ficar em branco.\n')

    tarefas.append({'nome':nome_tarefa})
    print(f'\nTarefa {nome_tarefa} adicionada com sucesso.\n')

    voltar_ao_menu_principal()

def listar_tarefas():
    '''Exibe todas as tarefas registradas.'''
    exibir_subtitulo('Listar Tarefas')

    for tarefa in tarefas:
        print(f'- {tarefa['nome']}')
    print('\nEssas são todas as tarefas registradas.\n')

    voltar_ao_menu_principal()

def remover_tarefa():
    '''Remove da lista a tarefa cujo nome o usuário informar.'''
    exibir_subtitulo('Remover Tarefa')

    digitou_algo = False
    while not digitou_algo:
        nome_tarefa = input('Digite o nome da tarefa que deseja remover: ').strip()

        if nome_tarefa:
            digitou_algo = True
        else:
            exibir_subtitulo('Remover Tarefa')
            print('\nO nome da tarefa não pode ficar em branco.\n')

    tarefa_encontrada = False        
    for tarefa in tarefas:
        if nome_tarefa == tarefa['nome']:
            tarefa_encontrada = True
            tarefas.remove(tarefa)
            print(f'\nTarefa {nome_tarefa} removida com sucesso.\n')
            break
    if not tarefa_encontrada:
        print('\nTarefa não encontrada\n')

    voltar_ao_menu_principal()

def finalizar_app():
    '''Exibe a mensagem de encerramento do aplicativo.'''
    exibir_subtitulo('Finalizando o app...')

def exibir_subtitulo(texto):
    '''Limpa a tela e exibe um subtítulo.

    Args:
        texto (str): texto do subtítulo.
    '''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    '''Avisa que a opção é inválida e volta ao menu principal.'''
    exibir_subtitulo('Opção Inválida.')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    '''Aguarda uma tecla do usuário e volta ao menu principal.'''
    input('Aperte qualquer botão para retornar ao menu principal. ')
    main()

def main():
    '''Limpa a tela, exibe o nome do app e o menu e lê a opção escolhida.'''
    os.system('cls')
    nome_do_app()
    opcoes()
    opcao_escolhida()

if __name__ == '__main__':
    main()