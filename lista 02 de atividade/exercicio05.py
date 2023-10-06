#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

a = int(input("insira a população do pais A"))
b = int(input("insria a população do pais B"))
ap = int(input("insria a taxa taxa de crescimento anual do pais A, (Ex: 3%) "))
bp = int(input("insira a taxa de crescimento anual do pais B, (Ex: 3%) "))

ano = 0

while a < b:
    a += a *ap *0.01
    b += b *bp *0.01
    ano += 1
 
print("A cidade A, levará" ,ano, "anos para superar a B")