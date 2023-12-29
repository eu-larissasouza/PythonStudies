# Funções e imports:
## Desenvolvido pela Luri: IA da Alura

# Escreva um programa em Python com uma função chamada "limpar_console()" que
# utilize a biblioteca "os" do Python para limpar o console antes de exibir uma
# mensagem. Você pode testar essa função chamando-a em um trecho de código e
# verificando se o console é limpo antes da mensagem ser exibida.

import os

print("EXERCICIO - FUNÇÕES E IMPORTS ================================\n")

nome = input("Qual seu nome: ")
idade = input("\nQual sua idade: ")

def limpar_console():
  os.system("cls")


limpar_console()
print(f"Olá, {nome}! Seja bem-vindo(a). Você tem {idade} anos.\n")