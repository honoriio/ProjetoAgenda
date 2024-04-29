from ..Colors.ColorsViews import Cores
from ..Lines.LinesViews import Lines

linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9, linha10 = Lines()

VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO, RESET = Cores()

def menuDeApresentacao():
    print(linha3)
    print(f'{MAGENTA}AGENDA DE CONTATOS{RESET} {VERDE}V1.1.2{RESET}'.center(120))
    print(linha3)


def Menu1():
    print(f'{CIANO}[1]{RESET}- {AZUL}Adicionar novo contato.{RESET}')
    print(f'{CIANO}[2]{RESET}- {AZUL}Ver lista de contatos.{RESET}')
    print(linha3)


def Menu2():
    print(linha3)
    print(f'{CIANO}[*]-{RESET}{AZUL}Selecione o contato{RESET}')
    print(linha3)


def Menu3():
    print(linha3)
    print(f'{CIANO}[1]-{RESET}{AZUL}Alterar Dados DO contato.{RESET}')
    print(f'{CIANO}[2]-{RESET}{AZUL}Deletar Contato.{RESET}')
    print(linha3)

def MenuAtualizacao():
    print(linha3)
    print(f'{CIANO}[1]-{RESET}{AZUL}Nome{RESET}')
    print(f'{CIANO}[2]-{RESET}{AZUL}Número{RESET}')
    print(f'{CIANO}[3]-{RESET}{AZUL}Email{RESET}')
    print(linha3)


    # REFATORAR AQUI TAMBEM