from libb.interface import *
from libb.interface.arquivo import *
from time import sleep

arq = '100atividades.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu([
        'Ver pessoas cadastradas',
        'Cadastrar nova pessoa',
        'Apagar pessoa cadastrada',
        'Sair do sistema'
    ])

    if resposta == 1:
        lerArquivo(arq)

    elif resposta == 2:
        cabecalho('NOVO CADASTRO')

        nome = input('Nome: ').strip()
        idade = leiaInt('Idade: ')

        cadastrar(arq, nome, idade)

    elif resposta == 3:
        apagarPessoa(arq)

    elif resposta == 4:
        cabecalho('Saindo do sistema... Até logo!')
        break

    else:
        print('\033[91mERRO! Digite uma opção válida.\033[m')

    sleep(2)