from peewee import * # ORM de banco de dados minimalista para python
import os

from Src.Views.Interface.InterfaceUsuario import MenuExcluirContato
from Src.Views.Lines.LinesViews import Lines
linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9, linha10 = Lines()

from Src.Views.Colors.ColorsViews import Cores
VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO, RESET = Cores()


db = SqliteDatabase('Src/Models/Agenda.db')

class Contato(Model):
    nome = CharField()
    numero = DecimalField(unique=True)
    email = CharField(unique=True)

    class Meta:
        database = db 



def CriarBancoDeDados():
    try:
        if not os.path.exists('Src/Models/Agenda.db'):
            db.connect()
            db.create_tables([Contato])
    except Exception as error:
        print(f'Erro ao criar banco de dados: {VERMELHO}{error}{RESET}')
    else:
        pass
    return CriarBancoDeDados
        

def CriarContato(nome, numero, email):
    try:
        contato = Contato.create(nome=nome, numero=numero, email=email)
    except Exception as error:
        print(f'Erro ao criar contato: {VERMELHO}{error}{RESET}')
    else: 
        print(f'{VERDE}Contato criado com sucesso!{RESET}')
        
    return CriarContato


def ExibirContatos():
    print(linha1)
    print('{:<5} {:<15} {:<15} {:<15}'.format("ID", "Nome", "Número", "Email"))
    print(linha1)
    
    try:
        for c in Contato.select():
            print('{:<5} {:<15} {:<15} {:<15}'.format(c.id, c.nome, c.numero, c.email))
    except Exception as error:
        print(f'A sua agenda esta vazia. Erro: {VERMELHO}{error}{RESET}')
    
    print(linha1)



def FiltrarContato():
    global contato_selecionado
    while True:
        try:
            id_contato = int(input('ID: '))
            contato_selecionado = Contato.get_or_none(Contato.id == id_contato)
            if contato_selecionado:
                print(linha1)
                print(f'{VERMELHO}Contato selecionado:{RESET} Nome: {VERDE}{contato_selecionado.nome}{RESET}, Número: {VERDE}{contato_selecionado.numero}{RESET}, Email: {VERDE}{contato_selecionado.email}{RESET}')
                return contato_selecionado
            else:
                print('ID do contato não encontrado. Tente novamente.')
        except ValueError:
            print('Por favor, digite um número válido.')
            


# Preciso mudar essa função..... fazer com que a mesma use a função filtrar para selecionar o contato
def AlterarContato():
    if not contato_selecionado:
        print('O contato selecionado não existe.')
        return
    
    
    print(linha3)
    print(f'{AZUL}Informe o que deseja alterar.{RESET}')
    print(linha3)
    print(f'{CIANO}[1]-{RESET}{AZUL}Nome{RESET}')
    print(f'{CIANO}[2]-{RESET}{AZUL}Número{RESET}')
    print(f'{CIANO}[3]-{RESET}{AZUL}Email{RESET}')
    print(linha3)
    opcao = input('Opção: ')
    
    escolha_usuario = input('Informe o novo dado: ')
    
    if opcao == '1':
        contato_selecionado.nome = escolha_usuario
    elif opcao == '2':
        contato_selecionado.numero = escolha_usuario
    elif opcao == '3':
        contato_selecionado.email = escolha_usuario
    else:
        print('Opção inválida.')
        return
    
    contato_selecionado.save()
    print('Contato Atualizado:', contato_selecionado.nome)


def ExcluirContato():
    try:
        print(linha1)
        print(f'Contato Selecionado {VERMELHO}Contato selecionado:{RESET} Nome: {VERDE}{contato_selecionado.nome}{RESET}, Número: {VERDE}{contato_selecionado.numero}{RESET}, Email: {VERDE}{contato_selecionado.email}{RESET}')
        print(linha1)
        print('Realmente Deseja Excluir o Contato Selecionado?')
        print(linha1)
        MenuExcluirContato()
        opc = input('Opção: ')
        if opc == '1':
            print('Contato excluído com sucesso.')
            contato_selecionado.delete_instance()
    except Contato.DoesNotExist:
        print('O contato selecionado não existe.')
    except Exception as error:
        print(f'Ocorreu um erro ao tentar excluir o contato selecionado erro: {VERMELHO}{error}{RESET}')
    finally:
        db.close()
