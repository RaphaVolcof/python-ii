saldo = 100
""""
deu certo a execução
while (saldo != 0):
    print('SALDO', saldo)
    saque = int(input("VALOR SAQUE:"))
    saldo = saldo - saque
    if saldo < 0:
     print("Não autorizado")
     break
"""
    
"""
jeito do professor
while (saldo != 0):
    print('SALDO', saldo)
    saque = int(input("VALOR SAQUE:"))
    saldo = saldo - saque
    if(saque <= saldo):
    else:
    print(f"SALDO DISPONÍVEL {saldo}")

"""
"""
depois vou testar em casa é o jeito q o prof fez
while (saldo != 0):
     print('SALDO', saldo)
     saque = int(input("VALOR SAQUE:"))
     saldo = saldo - saque
     if (saque <= saldo):
     else:
      print(f"SALDO DISPONÍVEL {saldo}")

"""
# PARA
numero_secreto = 82
total_de_tentativas = 3
for rodada in range(1, total_de_tentativas + 1):
    print("\nTentativa {:02d} de {:02d}".format(rodada,total_de_tentativas))

    tentativa = input("Tente acertar o número de 1 a 100:")
    print("Você digitou:", tentativa)
    tentativa_int = int(tentativa)

    if(tentativa_int < 1 or tentativa_int > 100):
        print("Tentativa INVÁLIDA! Somente números de 1 a 100!")
        continue  
    
    acerto = tentativa_int == numero_secreto
    if(acerto):
        print("Parabéns. ACERTOU!")
        break
    else:
        print("Não foi dessa vez. ERROU!")
      