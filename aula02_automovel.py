class Automovel:
    def __init__(self, cor, modelo, num_portas, tipo_cambio, placa, marca):
      self.cor = cor        
      self.modelo = modelo
      self.num_portas = num_portas
      self.tipo_cambio = tipo_cambio
      self.motor = False
      self.placa = placa
      self.marca = marca

    def ligar(self):
        if(self.motor == True):
            print("O CARRO JA ESTÁ LIGADO")
        else:    
             self.motor = True


carro = Automovel("Branca", "Corsa", "5", "Manual", "TITO2024", "GM")
print(carro.motor)
carro.ligar()
print(carro.motor)
carro.ligar()




