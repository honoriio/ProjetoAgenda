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
    for c in Contato:
        print(linha1)
        print("- ", c.id ,"Nome: ", c.nome, "Número: ", c.numero, "Email: ", c.email)
    print(linha1)
        



def AlterarContato():
    
#def ExcluirContato():

