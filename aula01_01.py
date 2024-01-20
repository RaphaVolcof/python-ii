"""
numero = int(input("Digite um número: "))
NUM = 32

#SE/SENAO

if numero == NUM:
    print("Voce Acertou o número!")
else:
    print("Você errou o número")    
    """

"""
se a media for maior ou = 7 mensagem aprovado, entre 4 e 6, recuperação, abaixo de 4 recuperação
"""



prova_1 = float(input ("Nota da primeira prova: "))
prova_2 = float(input ("Nota da segunda prova: "))
prova_3 = float(input ("Nota da terceira prova: "))
prova_4 = float(input ("Nota da quarta prova: "))

media = (prova_1 + prova_2 + prova_3 + prova_4) / 4 
print(media)

if media >= 7: 
    print('VOCE FOI APROVADO')
elif media <= 4:
    print('VOCE FOI REPROVADO')
else:
    print('RECUPERACAO')
    
""""

#jeito do professor
 #notas - media - situação
nota_1 = float(input ("Nota da primeira prova: "))
nota_2 = float(input ("Nota da segunda prova: "))
nota_3 = float(input ("Nota da terceira prova: "))
nota_4 = float(input ("Nota da quarta prova: "))

# media = (nota1 + nota2 + nota3 + nota4)//4
soma = nota_1 + nota_2 + nota_3 + nota_4
media = soma / 4

# se / senao se / senao
if (media >= 7): #media > 6
    print("Aprovado")
elif (media >= 4 or media <+6):
    print("Recuperação")
else:
    print("Reprovado")
    """

