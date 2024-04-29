from Src.Views.Interface.InterfaceUsuario import menuDeApresentacao, Menu1
from Src.Controlers.Functions import AcaoMenu1, NovoContato
from Src.Models.LogicaBancoDeDados import ChamarBancoDeDados

menuDeApresentacao()
Menu1()
AcaoMenu1()





# A parte da coleta e aramazenamento dos dados no dicionario COntatosIndividuais esta funcionando normalmente, o problema esta sendo na hora de atribuir os dados ao banco de dados