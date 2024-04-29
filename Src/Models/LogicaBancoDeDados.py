import sqlite3
from Src.Controlers.Functions import NovoContato # VERIFICAR

class BancoDeDados:
    def Conectar(self, BancoDeDadosContatos):
        self.conn = sqlite3.connect(BancoDeDadosContatos)

    def Desconectar(self):
        self.conn.close()

    def CriarTabela(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Contatos (
            id INTEGER PRIMARY KEY,
            Nome TEXT,
            Numero TEXT,
            Email TEXT,
            IdContato TEXT
        )
        ''')
        self.conn.commit()

    def InserirDados(self, ContatosIndividuais):
        cursor = self.conn.cursor()
        cursor.execute('''
        INSERT INTO Contatos (Nome, Numero, Email)
        VALUES (?,?,?)
        ''', (ContatosIndividuais['Nome'], ContatosIndividuais['Numero'], ContatosIndividuais['Email']))
        self.conn.commit()

    def ProcessarContatos(self):
        ContatosIndividuais = NovoContato()  # VERIFICAR
        self.InserirDados(ContatosIndividuais)


def ChamarBancoDeDados():
    bd = BancoDeDados()
    bd.Conectar('Src/Models/BancoDeDadosContatos.db')
    bd.CriarTabela()
    bd.ProcessarContatos(nome, numero, email)
    bd.Desconectar()




# NÃO ESTOU CONSEGUINDO ADICIONAR OS DADOS NO BANCO DE DADOS 