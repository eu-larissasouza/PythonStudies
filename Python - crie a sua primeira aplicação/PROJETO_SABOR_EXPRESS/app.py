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
## ------


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
#         # Código a ser executado se nenhum dos padrões anteriores corresponder.
#         # Isso é útil para tratar casos não específicos.
## ================================================================


## ================================================================
## AULA 03: LISTAS, LAÇOS E EXCEÇÕES

## ERROS

## Analisando e testando o programa, é possível identificar um problema
## na iteração que define ações para cada opção escolhida, o que lança um
## erro caso o usuário informe uma opção inválida, portanto a primeira coisa
## a ser feita é especificar que o app deve ser finalizado somente se for 4.

## TRY EXCEPT:

## Bloco try: permite testar um bloco de código em busca de erros.
## Bloco except: permite lidar com o erro.
## Bloco else: permite executar código quando não há erro.
## Bloco finally: executa código independentemente do resultado nos blocos try e except.

## LISTAS:

## Quando desejamos armazenar uma coleção de dados, podemos criar uma lista e
## diferente de outras linguagens em que é necessário especificar o tipo de
## dados para a lista, mas no Python não.

## Para adicionar um elemento na lista, utilizamos o append.
## ================================================================


## ================================================================
## AULA 04: DICIONÁRIOS

## Apesar de termos uma lista de dados contendo todos os nomes dos
## restaurantes, existem outras informações importantes que nós
## precisamos armazenar sobre cada restaurante, como categoria e
## se ele está (ou não) ativado, portanto utilizaremos a estrutura de
## dados dicionário e que tem funcionamento semelhante a uma estrutura
## que conhecemos como chave-valor em outras linguagens de programação.

## ================================================================



## ================================================================
## AULA 05: CONSOLIDANDO CONHECIMENTOS

## Uma ferramenta muito interessante que você pode inserir dentro das funções
## para torná-las mais descritivas são as chamadas docstrings, que tem como
## objetivo explicar um pouco do que aquela função está fazendo.

## Para criar uma docstring em Python, normalmente ela fica na primeira linha,
## logo após a definição da função e você pode usar três aspas.

## Um exemplo de docstring para a função cadastrar novo restaurante, seria:
##  """Essa função é responsável por cadastrar um novo restaurante"""

## Deste modo, qualquer pessoa que ler o código, vai entender o que a função
## faz, sem precisar analisar todo o código. A pessoa pode simplesmente ler
## essa frase e entender melhor o que a função faz.

## Além disso, também podemos criar docstrings mais complexas e que apresentem
## também quais inputs e outputs da função.

## ================================================================


restaurantes = [
    {"nome": "Praça", "categoria": "Japonesa", "ativo": False},
    {"nome": "Pizza Suprema", "categoria": "Italiano", "ativo": True},
]


def exibir_nome_do_programa():
    """ Exibe o nome estilizado do programa na tela """
    print(
        """
░█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ░█▀▀▀ █─█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
─▀▀▀▄▄ █▄▄█ █▀▀▄ █──█ █▄▄▀ 　 ░█▀▀▀ ▄▀▄ █──█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
░█▄▄▄█ ▀──▀ ▀▀▀─ ▀▀▀▀ ▀─▀▀ 　 ░█▄▄▄ ▀─▀ █▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀ ▀▀▀
      """
    )


def exibir_opcoes():
    """ Exibe as opções disponíveis no menu principal """
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Alternar Estado do Restaurante")
    print("4. Sair da aplicação\n")


def exibir_subtitulo(texto):
    """ Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    """
    os.system("cls")  ## Limpando o console
    linha = "-" * 2 * (len(texto))

    print(linha)
    print(texto)
    print(linha)
    print()


def voltar_ao_menu():
    """ Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    """    
    input("\nDigite qualquer tecla para voltar ao menu.\n")
    main()


def cadastrar_novo_restaurante():
    """ Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    """
    exibir_subtitulo("Cadastro de Novos Restaurantes.")

    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_restaurante}: ")

    dados_restaurante = {
        "nome": nome_restaurante.title(),
        "categoria": categoria.title(),
        "ativo": False,  # Todo restaurante é criado "inativo"
    }
    restaurantes.append(dados_restaurante)

    print(f"\nRestaurante {nome_restaurante} cadastrado com sucesso!\n")
    voltar_ao_menu()


def listar_restaurantes():
    """ Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    """
    exibir_subtitulo("Listando os Restaurantes")

    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status \n')

    # Usando a estrutura de repetição for
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"].title()
        categoria = restaurante["categoria"].title()
        ativo = f"Ativo" if restaurante["ativo"] is True else "Inativo"

        # Ljust: Função que define quantidade de caracteres a ser adicionado a esquerda
        print(f"{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltar_ao_menu()


def alternar_estado_restaurante():
    """ Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    """
    exibir_subtitulo("Alterando estado do restaurante")

    nome_restaurante = input(
        "Digite o nome do restaurante que deseja alterar o estado: "
    )
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante.upper() == restaurante["nome"].upper():
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]

            ## Operador Ternário em Python
            mensagem = (
                f"O restaurante {nome_restaurante.title()} foi ativado com sucesso"
                if restaurante["ativo"]
                else f"O restaurante {nome_restaurante.title()} foi desativado com sucesso"
            )
            print(mensagem)

    if not restaurante_encontrado:
        print("O restaurante não foi encontrado.")

    voltar_ao_menu()


def finalizar_app():
    """ Exibe mensagem de finalização do aplicativo """
    exibir_subtitulo("Encerrando programa....")


def opcao_invalida():
    """ Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    """
    print("\nA opção informada é inválida!\n")
    voltar_ao_menu()


def escolher_opcao():
    """ Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    """
    try:
        ## Variavel para armazenar opção - Valor inteiro
        opcao_escolhida = int(input("Escolha uma opção: "))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def main():
    """ Função principal que inicia o programa """
    os.system("cls")  ## Garante que a tela esteja limpa ao iniciar.
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == "__main__":
    main()
