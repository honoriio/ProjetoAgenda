#Area destinada as importações 
from Src.Views.Lines.LinesViews import Lines
linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9, linha10 = Lines()

from Src.Views.Colors.ColorsViews import Cores
VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO, RESET = Cores()

from Src.Models.LogicaBancoDeDados import *

from Src.Controlers.Validation import *

from Src.Models.LogicaBancoDeDados import CriarContato, CriarBancoDeDados, ExibirContatos

# Aqui se encontra as funções de logica para  entrada de dados do usuario


class Contato:
    def __init__(self,Nome, Email, Numero):
        self.Nome = Nome
        self.Email = Email
        self.Numero = Numero
        



def AcaoMenu1():
    print(MAGENTA + linha4 + RESET)
    opc = input('Opção: ')
    print(MAGENTA + linha4 + RESET)

    if opc == '1':
        NovoContato()
    elif opc == '2':
        ExibirContatos()


def AcaoMenu2():
    print(MAGENTA + linha4 + RESET)
    opc = input('Opção: ')
    print(MAGENTA + linha4 + RESET)

    if opc == '1':
        print('ok')
    elif opc == '2':
        print('ok')


def Nome():
    while True:
            nome = input('Nome: ')
            print(linha1)
            if ValidarNome(nome):
                break
    return nome


def Numero():
    while True:
        numero = input('Numero Celular: ')
        print(linha1)
        if ValidarNumero(numero):
            break
    return numero 


def Email():
    while True:
        email = input('Email: ')
        print(linha1)
        if ValidarEmail(email):
            break
    return email

    

def NovoContato():
    nome = Nome()
    numero = Numero()
    email = Email()
    #CriarBancoDeDados()
    CriarContato(nome, numero, email)


    
    

