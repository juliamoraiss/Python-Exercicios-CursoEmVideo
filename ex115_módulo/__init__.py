def menu():
    from time import sleep
    print('=' * 40)
    print(f'{"MENU PRINCIPAL":^40}')
    print('=' * 40)
    print('\033[33m1 -\033[m\033[34m Ver pessoas cadastradas')
    print('\033[33m2 -\033[m\033[34m Cadastrar nova pessoa')
    print('\033[33m3 -\033[m\033[34m Sair\033[m')
    print('=' * 40)
    try:
        opcao = int(input('\033[32mSua opção: \033[m'))
    except (TypeError, ValueError):
        print('\033[31mOpção inválida. Digite uma opção válida. \033[m')
        sleep(0.5)
    else:
        if opcao == 1:
            sleep(0.5)
            listar_pessoas()
        elif opcao == 2:
            sleep(0.5)
            cadastro_pessoa()
        elif opcao == 3:
            sleep(0.5)
            sair()
        else:
            print('\033[31mERRO! Digite uma opção válida. \033[m')
            sleep(0.5)


def listar_pessoas():
    from time import sleep
    print('=' * 40)
    print(f'{"PESSOAS CADASTRADAS":^40}')
    print('=' * 40)
    sleep(1)
    arquivo = open('ex115_módulo/bancopessoas.text', 'r', encoding='UTF-8')
    f = arquivo.readlines()
    for linhas in f:
        nome = linhas.split(';')[0]
        idade = linhas.split(';')[1]
        print(f'{nome:<33}{idade}')


def cadastro_pessoa():
    from time import sleep
    arquivo = open('ex115_módulo/bancopessoas.text', 'r', encoding='UTF-8')
    conteudo = arquivo.readlines()
    conteudo.append('\n')
    nome = str(input('Nome: '))
    conteudo.append(nome)
    conteudo.append(';')
    while True:
        try:
            idade = int(input('Idade: '))
            conteudo.append(str(idade))
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um número inteiro válido. \033[m')
        else:
            conteudo.append(' anos')
            arquivo = open('ex115_módulo/bancopessoas.text', 'w', encoding='UTF-8')
            arquivo.writelines(conteudo)
            arquivo.close()
            sleep(0.5)
            print(f'\033[32mRegistro de {nome} adicionado!\033[m')
            sleep(0.5)
            break


def sair():
    from time import sleep
    print('\033[35m=' * 40)
    print(f'{"SAINDO DO SISTEMA... VOLTE SEMPRE!":^40}')
    print('=' * 40)
    sleep(0.5)
    exit()
