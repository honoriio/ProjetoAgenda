from peewee import * # ORM de banco de dados minimalista para python

from Src.Views.Lines.LinesViews import Lines
linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9, linha10 = Lines()

db = SqliteDatabase('Src/Models/BancoDeDadosContatos.db')

class Contato(Model):
    nome = CharField()
    numero = DecimalField(unique=True)
    email = CharField(unique=True)

    class Meta:
        database = db 



def CriarBancoDeDados():
    try:
        db.connect()
        db.create_tables([Contato])
    except Exception as error:
        print(f'Erro ao criar banco de dados: {error}')
    else:
        print(f'Banco de dados criado com sucesso!')
    return CriarBancoDeDados
        

def CriarContato(nome, numero, email):
    try:
        contato = Contato.create(nome=nome, numero=numero, email=email)
    except Exception as error:
        print(f'Erro ao criar contato: {error}')
    else: 
        print('Contato criado com sucesso!')
        
    return CriarContato


def ExibirContatos():
    print(linha3)
    print(linha1)
    print("{:<5} {:<15} {:<15} {:<15}".format("ID", "Nome", "Número", "Email"))
    print(linha1)
    
    for c in Contato.select():
        print("{:<5} {:<15} {:<15} {:<15}".format(c.id, c.nome, c.numero, c.email))
    
    print(linha1)



def FiltrarContato():
   while True:
    try:
        id_contato = int(input('ID: '))
        contato_selecionado = Contato.get_or_none(Contato.id == id_contato)
        if contato_selecionado:
    
            print(linha1)
            print("Contato selecionado:", contato_selecionado.nome)
            print(linha1)
            break
        else:
            print("ID do contato não encontrado. Tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")
        
        return contato_selecionado



# Entender o que essa parte faz exatamente, pois foi corrigida pelo gpt
def AlterarContato():
    contato_selecionado = input('Informe o nome do contato que deseja alterar: ')
    try:
        contato = Contato.get(Contato.nome == contato_selecionado)
    except Contato.DoesNotExist:
        print("O contato selecionado não existe.")
        return
    
    opcao = input('Informe o que deseja alterar (nome/número/email): ')
    escolha_usuario = input('Informe o novo dado: ')
    
    if opcao == 'nome':
        contato.nome = escolha_usuario
    elif opcao == 'número':
        contato.numero = escolha_usuario
    elif opcao == 'email':
        contato.email = escolha_usuario
    else:
        print("Opção inválida.")
        return
    
    contato.save()
    print('Contato Atualizado:', contato)






#def ExcluirContato():
