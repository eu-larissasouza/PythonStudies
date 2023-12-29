# Hora da Prática: função condicionais 
## Lista 02 de Exercicios

# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura
# if else para determinar se o número é par ou ímpar..
# print("\nExercício 01 ========================================================")

numero = int(input("Informe um número: "))

if (numero % 2) == 0:
  print(f"\nO número {numero} é par\n")
else:
  print(f"\nO número {numero} é ímpar\n")


# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para
# classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

print("\nExercício 02 ========================================================")

idade = int(input("Qual sua idade: "))

if 0 < idade <= 12:
  print("\nVocê é uma criança!\n")
elif 12 < idade <= 18:
  print("\mVocê é um adolescente!\n")
elif idade >= 18:
  print("\nVocê é um adulto!\n")
else:
  print("\nIdade Inválida!\n")



# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o 
# nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

print("\nExercício 03 ========================================================")

USUARIO = "lasouza"
SENHA = "abc19682X"

seu_usuario = input("Informe o seu usuário: ")
sua_senha = input("Informe a sua senha: ")

if (seu_usuario == USUARIO and sua_senha == SENHA):
  print("\nLogin efetuado com sucesso!\n")
else:
  print("\nO usuário ou senha informados estão incorretos.\n")


# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura
# if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de
# acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

print("\nExercício 04 ========================================================")

x = int(input("Informe o valor para o eixo X: "))
y = int(input("Informe o valor para o eixo Y: "))

if x > 0 and y > 0:
  print(f"\nCoordenadas ({x},{y}) estão localizadas no primeiro quadrante!\n")
elif x < 0 and y > 0:
  print(f"\nCoordenadas ({x},{y}) estão localizadas no segundo quadrante!\n")
elif x < 0 and y < 0:
  print(f"\nCoordenadas ({x},{y}) estão localizadas no terceiro quadrante!\n")
elif x > 0 and y < 0:
  print(f"\nCoordenadas ({x},{y}) estão localizadas no quarto quadrante!\n")
else:
  print(f"\nCoordenadas ({x},{y}) estão localizadas no eixo ou origem!\n")
