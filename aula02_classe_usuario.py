class Usuario:
     def __init__(self, nome, idade, cidade, etnia):  
        self.nome = nome 
        self.idade = idade
        self.cidade = cidade
        self.etnia = etnia

cliente = Usuario(nome=input("QUAL O SEU NOME"),
                  idade=input("QUAL A SUA IDADE?:"),
                  cidade=input("QUAL CIDADE VOCÊ MORA?"),
                  etnia=input("QUAL SUA ETNIA?:"))


print (cliente.cidade)

