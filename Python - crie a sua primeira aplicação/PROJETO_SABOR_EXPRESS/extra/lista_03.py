# Hora da Prática: listas, for e try except
## Lista 03 de Exercicios

# 1 - Crie uma lista para cada informação a seguir:

# -> Lista de números de 1 a 10;
# -> Lista com quatro nomes;
# -> Lista com o ano que você nasceu e o ano atual.

print("\nExercício 01 ========================================================\n")

lista_numerica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_nomes = ["Larissa", "Katharine", "Isabelle", "Jéssica"]
lista_anos = [2004, 2024]


# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

print("\nExercício 02 ========================================================\n")

lista_de_youtubers = ["Jean Luca", "Jessica Balut", "Thaissa Balut"]

for youtuber in lista_de_youtubers:
    print(f"Youtuber {youtuber}\n")


# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

print("\nExercício 03 ========================================================\n")

soma = 0

for num in range(1, 10):
    if num % 2 != 0:
        soma += num

print(f"Soma dos números ímpares de 1 a 10: {soma}\n")


# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

print("\nExercício 04 ========================================================\n")

for num in range(10, 0, -1):
    print(num)


# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para
# imprimir a tabuada desse número, indo de 1 a 10.

print("\nExercício 05 ========================================================\n")

numero_tabuada = int(input("Informe um número: "))

print(f"\nTabuada do {numero_tabuada}:\n")

for num in range(1, 11):
    resultado = numero_tabuada * num
    print(f"{numero_tabuada} x {num} = {resultado}")


# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de
# todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

print("\nExercício 06 ========================================================\n")

lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")


# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize
# um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

print("\nExercício 07 ========================================================\n")

lista_valores = [5, 15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor

    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
