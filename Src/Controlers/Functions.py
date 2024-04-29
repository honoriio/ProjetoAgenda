#Area destinada as importações 
from Src.Views.Lines.LinesViews import Lines
linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9, linha10 = Lines()

from Src.Models.LogicaBancoDeDados import *

from Src.Controlers.Validation import *

# Aqui se encontra as funções de logica para  entrada de dados do usuario


class Contato:
    def __init__(self,Nome, Email, Numero):
        self.Nome = Nome
        self.Email = Email
        self.Numero = Numero
        

ContatosIndividuais = {}

def AcaoMenu1():
    opc = input('Opção: ')

    if opc == '1':
        NovoContato()
    elif opc == '2':
        print(BancoDeDadosContatos.db)


def Nome():
    while True:
            nome = input('Nome: ')
            print(linha1)
            if ValidarNome(nome):
                ContatosIndividuais['Nome'] = nome
                break
    return Nome


def Numero():
    while True:
        numero = input('Numero Celular: ')
        print(linha1)
        if ValidarNumero(numero):
            ContatosIndividuais['Numero'] = numero
            break
    return Numero 


def Email():
    while True:
        email = input('Email: ')
        print(linha1)
        if ValidarEmail(email):
            ContatosIndividuais['Email'] = email
            break
    return Email

    

def NovoContato():
    Nome()
    Numero()
    Email()
    print(ContatosIndividuais)
    ChamarBancoDeDados()

    return Nome, Numero, Email
    

