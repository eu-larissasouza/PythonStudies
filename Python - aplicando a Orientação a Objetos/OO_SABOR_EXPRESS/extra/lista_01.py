# Hora da Prática: Instância de uma Classe
## Lista 01 de Exercicios


class Restaurante:
    Nome = ""
    Categoria = ""
    Ativo = False


restaurante_praca = Restaurante()
restaurante_praca.Nome = "Praça"
restaurante_praca.Categoria = "Gourmet"

# 1 - Atribua o valor "Italiana" ao atributo categoria da instância
# restaurante_praca da classe Restaurante.

print("\nExercício 01 ========================================================\n")

restaurante_praca.Categoria = "Italiana"

print(restaurante_praca.Categoria)

# 2 - Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

print("\nExercício 02 ========================================================\n")

print(restaurante_praca.Nome)

# 3 - Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba
# uma mensagem informando se o restaurante está ativo ou inativo.

print("\nExercício 03 ========================================================\n")

if restaurante_praca.Ativo:
    print("O restaurante está ativo.")
else:
    print("O restaurante está inativo.")


# 4 - Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene
# em uma variável chamada categoria.

print("\nExercício 04 ========================================================\n")

categoria = Restaurante.Categoria

# 5 - Altere o valor do atributo nome para "Bistrô".

print("\nExercício 05 ========================================================\n")

restaurante_praca.Nome = "Bistrô"

print(restaurante_praca.Nome)


# 6 - Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o
# nome "Pizza Place" e categoria "Fast Food".

print("\nExercício 06 ========================================================\n")

restaurante_pizza = Restaurante()

restaurante_pizza.Nome = "Pizza Place"
restaurante_pizza.Categoria = "Fast Food"

print(vars(restaurante_pizza))


# 7 - Verifique se a categoria da instância restaurante_pizza é "Fast Food".

print("\nExercício 07 ========================================================\n")

if restaurante_pizza.Categoria == "Fast Food":
    print("A categoria é Fast Food.")
else:
    print("A categoria não é Fast Food.")


# 8 - Mude o estado da instância restaurante_pizza para ativo.

print("\nExercício 08 ========================================================\n")

restaurante_pizza.Ativo = True

print(restaurante_pizza.Ativo)


# 9 - Imprima no console o nome e a categoria da instância restaurante_praca.

print("\nExercício 09 ========================================================\n")

print(
    f"Restaurante: {restaurante_praca.Nome} - Categoria: {restaurante_praca.Categoria}"
)
