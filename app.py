from Src.Views.Lines.LinesViews import Lines
from Src.Views.Colors.ColorsViews import Cores

linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9, linha10 = Lines()
VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO, RESET = Cores()

print(AZUL + linha1 + RESET)