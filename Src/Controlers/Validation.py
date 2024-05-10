# Aréa Destinada a imporação 
from Src.Views.Colors.ColorsViews import Cores
VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO, RESET = Cores()

from Src.Views.Lines.LinesViews import Lines
linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9, linha10 = Lines()
import unidecode
import re

# Aqui se encontra toda a logica para validações das entradas do usuario

def ValidarNome(nome):
    TamanhoNome = 50
    TamanhoNomeContato = len(nome)
    if TamanhoNomeContato > TamanhoNome:
        print(f'{AMARELO}Tamanho de {TamanhoNome} Caracteres Excedido.{RESET}')
        print(linha1)
    else: 
        return True

def ValidarNumero(Numero):
    caracteres_permitidos = set("1234567890")
    if all(char in caracteres_permitidos for char in Numero):
        tam_numero = 11
        tam_numero_usuario = len(Numero)
        if tam_numero_usuario == tam_numero:
            return True
        else:
            print(f'{VERMELHO}O número informado é inválido. Por favor, insira um número válido.{RESET}')
            print(linha1)
    else:
        print(f'{VERMELHO}O número informada contém caracteres não permitidos. Por favor, insira apenas números, sem barra, aspas ou ponto de separação.{RESET}')
        print(linha1)
    return False


def ValidarEmail(email):
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
     
    if re.match(padrao, email):
        return True
    else:
        print(f'{AMARELO}O Email digitado esta incorreto.{RESET}')
        return False
