#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite o seu nome: ")
while len(nome) <= 3:
    nome = input("O nome deve ter mais de 3 caracteres. Digite novamente: ")

idade = int(input("Insira a sua idade"))
while idade <0 or idade >150:
    idade = input("como vc vai ter essa idade animal, digita mais uma vez ai:")
    
    salario = int(input("insira o seu salario"))
    while salario <0:
        salario = int(input("como ganha menos q 0 amigo, tenta mais uma vez:"))
        
sexo = input("Digite o seu sexo (f/m): ")
while sexo != 'f' and sexo != 'm':
    sexo = input("O sexo deve ser 'f' ou 'm'. Digite novamente: ")

estado_civil = input("Digite o seu estado civil (s/c/v/d): ")
while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input("O estado civil deve ser 's', 'c', 'v' ou 'd'. Digite novamente: ")
    