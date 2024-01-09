# Hora da Prática: dicionários
## Lista 04 de Exercicios

# 1 - Crie um dicionário representando informações sobre uma
# pessoa, como nome, idade e cidade.

print("\nExercício 01 ========================================================\n")

nome_pessoa = input("Informe o seu nome: ")
idade_pessoa = int(input("Informe sua idade: "))
cidade_pessoa = input("Informe sua cidade: ")

dados_pessoa = {"nome": nome_pessoa, "idade": idade_pessoa, "cidade": cidade_pessoa}

print(f"\nPessoa: {dados_pessoa["nome"]} | Idade: {dados_pessoa["idade"]} | Cidade: {dados_pessoa["cidade"]} \n")


# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.

print("\nExercício 02 ========================================================\n")

# Atualização de Idade
dados_pessoa["idade"] = 20

# Adicionando Profissão
dados_pessoa["profissao"] = "Analista de Dados"

# Remoção de Elementos
del dados_pessoa["cidade"]

print(f"Pessoa: {dados_pessoa["nome"]} | Idade: {dados_pessoa["idade"]} | Profissão: {dados_pessoa["profissao"]} \n")


# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.

print("\nExercício 03 ========================================================\n")

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)


# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

print("\nExercício 04 ========================================================\n")

nome_buscado = input("Informe um nome para buscar no dicionário: ")

pessoa = {"nome": "Amanda", "idade": 19, "cidade": "São Luís"}

if nome_buscado == pessoa["nome"]:
    print(f"A chave {nome_buscado} existe no dicionário.\n")
else:
    print(f"A chave {nome_buscado} não existe no dicionário.\n")


# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

print("\nExercício 05 ========================================================\n")

frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()

for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

print(contagem_palavras)
