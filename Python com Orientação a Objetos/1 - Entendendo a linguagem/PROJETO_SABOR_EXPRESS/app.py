## PRIMEIRA APLICAÇÃO EM PYTHON
## PROJETO SABOR EXPRESS

import os


## ================================================================
## AULA 01: MANIPULAÇÃO DE STRINGS

## RESUMO GERAL:

## Função print: Exibe informação
## Função input: Receber informação do usuário

## Aspas simples ou duplas: Escolha uma Convenção em cada projeto.
## Aspas triplas (usando simples ou duplas): Se queremos que a quebra de linha seja mantida no terminal

## Site FSymbols: Pode ser usado para adicionar formatação diferentes a titulo 
## É uma ideia, pois adiciona fontes chamativas e/ou engraçadas ao terminal.
## ------


## SOBRE INTERPOLAÇÃO DE STRINGS:

## Interpolação de Strings: Adicionar variável ao texto
## Forma mais elegante: Utilizando a formatação f-string

## Vantagem: Definir as formatação de uma forma mais legível.
## print(f"Você escolheu a opção {opcao_escolhida}!")
## ================================================================


## ================================================================
## AULA 02: MÓDULOS E FUNÇÕES

## SOBRE CONDICIONAIS

## Em um primeiro momento, todas as execuções levam ao else,
## independente da opção escolhida via terminal...

## Isso acontece, porque por padrão, o Python define as variaveis
## como valores do tipo Strings e como é uma linguagem fortemente tipada
## não tem como comparar valores de tipos diferentes

## Para verificar o tipo, usamos a função type(): 
## print(type(opcao_escolhida))

## Lembrete: ELIF - equivalente ao else if em outras linguagens
## ------


## SOBRE FUNÇÕES E IMPORTS:

## O ideal seria isolar um determinado comportamento em uma sequência de código.
## Isso nos ajuda a manter o código atualizado, a editá-lo e assim por diante.

## Podemos usar um recurso que é criar funções, isto é, um bloco de código
## que tem o objetivo de realizar uma função.

## Usamos o def que é uma notação para "definir" a função

## Além disso, podemos utilizar algumas funções embutidas do Python. 
## No entanto, quando instalamos o Python na nossa máquina, ele também nos dá
## acesso a algumas bibliotecas com códigos prontos para utilizar.
## Uma dessas bibliotecas é a Biblioteca os.
## ------


## APROFUNDANDO FUNÇÕES

## Antes de criar essas opções, é importante entender que quando criamos
## um arquivo com a extensão .py, podemos ter indicar para o Python que
## esse é o arquivo principal do programa e garantir que ele não seja 
## importado por outros arquivos Python para que seja executado,
## assim como fizemos com o import os.
      
## Quando pedimos para que um programa Python seja executado, o interpretador
## cria uma variável chamada __name__ e podemos definir o programa como principal
## se o __name__ for __main__ (principal, em inglês),

## Assim, quando o Python executar e verificar que este arquivo aqui é o __main__,
## queremos que uma sequência de ações seja executada ou seja, a função main() terá 
## todos os passos que precisamos para que o nosso programa funcione
## ================================================================


def exibir_nome_do_programa():
      print("""
░█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ░█▀▀▀ █─█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
─▀▀▀▄▄ █▄▄█ █▀▀▄ █──█ █▄▄▀ 　 ░█▀▀▀ ▄▀▄ █──█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
░█▄▄▄█ ▀──▀ ▀▀▀─ ▀▀▀▀ ▀─▀▀ 　 ░█▄▄▄ ▀─▀ █▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀ ▀▀▀
      """)


def exibir_opcoes():
      print("1. Cadastrar Restaurante")
      print("2. Listar Restaurante")
      print("3. Ativar Restaurante")
      print("4. Sair da aplicação\n")


def finalizar_app():
      os.system("cls") ## Limpando o console
      print("Encerrando programa....\n")

## ================================================================
## INSTRUÇÃO MATCH

## Outra alternativa para o padrão if elif else é a função match que é a 
## abordagem correspondente ao switch(case) presente em muitas outras
## linguagens de programação
      
## Oferece uma abordagem mais elegante para a correspondência de padrões em dados.
## Essa adição não apenas simplifica a lógica do código, mas também proporciona 
## uma alternativa expressiva e legível às construções tradicionais de controle
## de fluxo, que são necessários para adaptar o comportamento do programa.
      
## Estrutura básica:  
      
# match expressão:
#     case padrão_1:
#         # Código a ser executado se expressão corresponder a padrão_1
#     case padrão_2:
#         # Código a ser executado se expressão corresponder a padrão_2
#     # ... outros casos ...
#     case _:
#         # Código a ser executado se nenhum dos padrões anteriores corresponder. Isso é útil para tratar casos não específicos.
## ================================================================
      

def escolher_opcao():
      ## Variavel para armazenar opção - Valor inteiro
      opcao_escolhida = int(input("Escolha uma opção: "))

      if opcao_escolhida == 1:
            print("Cadastrar restaurante")
      elif opcao_escolhida == 2:
            print("Listar Restaurante")
      elif opcao_escolhida == 3:
            print("Ativar Restaurante")
      else:
            finalizar_app()

      
def main():
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcao()


if __name__ == "__main__":
      main()
