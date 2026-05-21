from libb.interface import cabecalho, linha, leiaInt


def arquivoExiste(nome):
    try:
        with open(nome, 'rt', encoding='utf-8'):
            return True

    except FileNotFoundError:
        return False


def criarArquivo(nome):
    try:
        with open(nome, 'wt+', encoding='utf-8'):
            pass

    except Exception as erro:
        print(f'Erro ao criar arquivo: {erro}')

    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        with open(nome, 'rt', encoding='utf-8') as a:
            cabecalho('PESSOAS CADASTRADAS')

            for linhaArquivo in a:
                dado = linhaArquivo.split(';')
                dado[1] = dado[1].replace('\n', '')

                print(f'{dado[0]:<30}{dado[1]:>3} anos')

    except Exception as erro:
        print(f'Erro ao ler arquivo: {erro}')


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        with open(arq, 'at', encoding='utf-8') as a:
            a.write(f'{nome};{idade}\n')

    except Exception as erro:
        print(f'Erro ao cadastrar pessoa: {erro}')

    else:
        print(f'Novo registro de {nome} adicionado com sucesso!')


def apagarPessoa(nome):
    try:
        with open(nome, 'rt', encoding='utf-8') as a:
            pessoas = a.readlines()

    except Exception as erro:
        print(f'Erro ao ler arquivo: {erro}')
        return

    if len(pessoas) == 0:
        print('Não há pessoas cadastradas!')
        return

    cabecalho('APAGAR PESSOA CADASTRADA')

    for i, pessoa in enumerate(pessoas):
        dado = pessoa.split(';')
        dado[1] = dado[1].replace('\n', '')

        print(f'{i + 1} - {dado[0]:<30}{dado[1]:>3} anos')

    print(linha())

    opcao = leiaInt('Qual pessoa deseja apagar? ')

    if opcao < 1 or opcao > len(pessoas):
        print('Opção inválida!')
        return

    removido = pessoas.pop(opcao - 1)

    try:
        with open(nome, 'wt', encoding='utf-8') as a:
            for pessoa in pessoas:
                a.write(pessoa)

    except Exception as erro:
        print(f'Erro ao atualizar arquivo: {erro}')

    else:
        nomeRemovido = removido.split(';')[0]
        print(f'{nomeRemovido} foi removido com sucesso!')