from ..Colors.ColorsViews import Cores
from ..Lines.LinesViews import Lines

linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9, linha10 = Lines()

VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO, RESET = Cores()

def menuDeApresentacao():
    print(linha3)
    print(f'{AZUL}AGENDA DE CONTATOS{RESET} {VERDE}V1.1.2{RESET}'.center(80))
    print(linha3)
