#Area destinada as importações 
from Src.Views.Lines.LinesViews import Lines
linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9, linha10 = Lines()

from Src.Views.Colors.ColorsViews import Cores
VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO, RESET = Cores()

import time

import sys

from Src.Models.LogicaBancoDeDados import *

from Src.Controlers.Validation import *

from Src.Models.LogicaBancoDeDados import CriarContato, CriarBancoDeDados, ExibirContatos, FiltrarContato, ExcluirContato

from Src.Views.Interface.InterfaceUsuario import *

# Aqui se encontra as funções de logica para  entrada de dados do usuario


class Contato:
    def __init__(self,Nome, Email, Numero):
        self.Nome = Nome
        self.Email = Email
        self.Numero = Numero
        

# Ações dos menus de iteração

def AcaoMenu1(): # Menu de apresentação Para criação dos contatos
    while True:
        LimpaTela()
        menuDeApresentacao()
        Menu1()
        opc = input('Opção: ')

        if opc == '1':
            LimpaTela()
            MenuAdcionarContato()
            NovoContato()

        elif opc == '2':
            while True:  # Loop para exibir os contatos e permitir voltar
                LimpaTela()
                MenuListaDeContatos()
                ExibirContatos()
                Menu2()
                opc = input('Opção: ')
                if opc == '1':
                    print(MAGENTA + linha3 + RESET)
                    FiltrarContato()
                    print(MAGENTA + linha3 + RESET)
                    Menu3()
                    opc = input('Opção: ')
                    if opc == '1':
                        LimpaTela()
                        AlterarContato()  #Acrescentar um menu de seleção aqui para selecionar entre alterar ou excluir contato
                        time.sleep(1)
                        break
                    elif opc == '2':
                        ExcluirContato()
                        time.sleep(1)
                        break
                elif opc  == '2':
                    break  # Sai do loop de exibição e volta ao menu anterior
                else:
                    print(f'{VERMELHO}Opção inválida!{RESET}')
        elif opc == '3':
            LimpaTela()
            print(VERMELHO + linha3 + RESET) 
            print(f'{VERMELHO}Programa encerrado{RESET}'.center(100))
            print(VERMELHO + linha3 + RESET)
            time.sleep(2)
            LimpaTela()
            sys.exit()



def AcaoMenu2(): # seleção do contato para alterações posteriormente
    Menu2()
    print(MAGENTA + linha4 + RESET)
    FiltrarContato()
    print(MAGENTA + linha4 + RESET)

    


def AcaoMenu3(): # Menu de alteração dos contatos
    Menu3()
    print(MAGENTA + linha4 + RESET)
    opc = input('Opção: ')
    print(MAGENTA + linha4 + RESET)

    if opc == '1':
        #MenuAtualizacao()    #VERIFICAR
        AlterarContato() 
    elif opc == '2':
        ExcluirContato()


#def AcaoMenuAtualizacao():  PRECISO TERMINAR ESSA FUNÇÃO


def LimpaTela():
    import platform
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


# Coleta dos dados do usuario

def Nome():
    while True:
            nome = input('Nome: ')
            print(linha1)
            if ValidarNome(nome):
                break
    return nome


def Numero():
    while True:
        numero = input('Numero Celular: ')  #(Foi alterado de string para inteiro)    DEVO VERIFICAR TODAS AS FUNÇÕES DE VALIDAÇÃO, POIS TEMOS QUE ACRESCETAR TRATAMENTOS DE ERROS
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
    CriarBancoDeDados()
    CriarContato(nome, numero, email)


def Main():
    AcaoMenu1()

    
    

# VERIFICAR SE AS FUNÇÕES ESTAO CORRETAS