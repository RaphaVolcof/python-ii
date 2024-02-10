class Pessoas:

    seq = 0
    pessoas = []

    def __init__(self, nome, dataNasc, cpf, filiacao1, filiacao2):
        self.id = None
        self.nome = nome
        self.dataNasc = dataNasc
        self.cpf = cpf
        self.filiacao1 = filiacao1
        self.filiacao2 = filiacao2 

    def salvar(self):
        self.__class__.seq += 1
        self.id = self.__class__.seq
        self.pessoas.append(self)
       
    """"
        Pessoas.seq += 1
        self.id = Pessoas.seq
        Pessoas.pessoas.append(self)    
    """
       
    def __repr__(self):
        return "ID: {} - NOME: {} - DATA NASC.: {} - CPF: {} - FILIAÇÃO 1: {} - FILIAÇÃO 2: {} \n".format(self.id, self.nome, self.dataNasc, self.cpf, self.filiacao1, self.filiacao2)
   
    @classmethod
    def listar(cls):
        return cls.pessoas        

while True:

    pessoa1= Pessoas(input("Digite o seu nome: "),
                    input("Qual sua data de nascimento?: "),
                    input("Qual o seu cpf?:"),
                    input("Qual o nome da sua mãe?:"),
                    input("Qual o nome do seu pai?:")) 
    pessoa1.salvar() 
    print(Pessoas.listar()) 


    continuar_cadastro= (int(input("Deseja continuar os cadastros? Digite 1 para Sim e 2 para Não:")))
    if continuar_cadastro == 1:
        continue
    else: break 
    
print(Pessoas.listar()) 
   
