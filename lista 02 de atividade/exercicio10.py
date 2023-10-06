#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input("digite o primeiro numero"))
num2 = int(input("digite o segundo numero"))

max = (num1, num2)
min = (num1, num2)

for i in range(num1+1,num2):
    print(i)