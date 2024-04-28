#Area destinada as importações 
from Src.Views.Lines.LinesViews import Lines
linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9, linha10 = Lines()

from Src.Controlers.Validation import *

# Aqui se encontra as funções de logica para  entrada de dados do usuario


class Contato:
    def __init__(self,Nome, Email, Numero, Organizacao, ):
        self.Nome = Nome
        self.Email = Email
        self.Numero = Numero
        self.Organizacao = Organizacao



def AcaoMenu1():
    opc = input('Opção: ')

    if opc == '1':
        NovoContato()


def Nome():
    while True:
            nome = input('Nome: ')
            print(linha1)
            if ValidarNome(nome):
                break
    return Nome


def Numero():
    while True:
        numero = input('Numero Celular: ')
        print(linha1)
        if ValidarNumero(numero):
            break
    return Numero 


def Email():
    while True:
        email = input('Email: ')
        print(linha1)
        if ValidarEmail(email):
            break
    return Email

    

def NovoContato():
    Nome()
    Numero()
    Email()

    return Nome, Numero, Email
    

