# Manipulação de Strings e Interpolação de String:
## Desenvolvido pela Luri: IA da Alura

# Escreva um programa em Python que solicite ao usuário seu nome e sua idade. 
# Em seguida, exiba uma mensagem de boas-vindas personalizada, como por exemplo:
# "Olá, [nome]! Seja bem-vindo(a). Você tem [idade] anos."

print("EXERCICIO - INTERPOLAÇÃO DE STRINGS ================================\n")

nome = input("Qual seu nome: ")
idade = input("\nQual sua idade: ")

print(f"Olá, {nome}! Seja bem-vindo(a). Você tem {idade} anos.")