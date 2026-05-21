def leiaInt(msg):
    while True:
        try:
            numero = int(input(msg))

        except ValueError:
            print('\033[91mERRO! Digite um número inteiro válido.\033[m')

        except KeyboardInterrupt:
            print('\n\033[91mUsuário preferiu não informar o número.\033[m')
            return 0

        else:
            return numero


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')

    for c, item in enumerate(lista, start=1):
        print(f'\033[93m{c}\033[m - \033[94m{item}\033[m')

    print(linha())

    opcao = leiaInt('\033[92mSua opção: \033[m')

    return opcao