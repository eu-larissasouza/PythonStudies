# Projeto Sabor Express 

## Função print: Exibe informação
## Função input: Receber informação do usuário

## Aspas simples ou duplas: Escolha uma Convenção em cada projeto.
## Aspas triplas (usando simples ou duplas): Se queremos que a quebra de linha seja mantida no terminal

## Site FSymbols: Pode ser usado para adicionar formatação diferentes a titulo 
## É uma ideia, pois adiciona fontes chamativas e/ou engraçadas ao terminal.

print("""
░█▀▀▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀█ 　 ░█▀▀▀ █─█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ 
─▀▀▀▄▄ █▄▄█ █▀▀▄ █──█ █▄▄▀ 　 ░█▀▀▀ ▄▀▄ █──█ █▄▄▀ █▀▀ ▀▀█ ▀▀█ 
░█▄▄▄█ ▀──▀ ▀▀▀─ ▀▀▀▀ ▀─▀▀ 　 ░█▄▄▄ ▀─▀ █▀▀▀ ▀─▀▀ ▀▀▀ ▀▀▀ ▀▀▀
      """)

print("1. Cadastrar Restaurante")
print("2. Listar Restaurante")
print("3. Ativar Restaurante")
print("4. Sair da aplicação\n")

## Variavel para armazenar opção
opcao_escolhida = input("Escolha uma opção: ")

## Interpolação de Strings: Adicionar variável ao texto
## Forma mais elegante: Utilizando a formatação f-string
## Vantagem: Definir as formatação de uma forma mais legível.
print(f"Você escolheu a opção {opcao_escolhida}!")


