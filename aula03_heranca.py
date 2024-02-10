class Animal:
 def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

 def falar(self):
     print(f"O {self.nome} está falando!")  


class Cachorro(Animal):
   def __init__(self, nome, idade, raca):
      super().__init__(nome, idade)  
      self.raca = raca

   def latir(self):  
      print(f"O {self.nome} está latindo!")  

""""
meu_cachorro = Cachorro("Caramelo", 1, "Vira Lata")
print(meu_cachorro.nome) 
print(meu_cachorro.idade)  
meu_cachorro.falar()

print(meu_cachorro.raca)
meu_cachorro.latir()
"""
class Ave(Animal):
   def __init__(self, nome, idade,cor):
      super().__init__(nome, idade)
      self.cor = cor
   def falar(self):
      print(f"O {self.nome} não para de falar!")

minha_ave = Ave("Loreco", 15, "Verde")
print(minha_ave.nome) 
print(minha_ave.idade)  
print(minha_ave.cor)
minha_ave.falar()      
