# Hora da Prática: função print ()

## 1 - Imprima a frase: Python na Escola de Programação da Alura.
print("\nExercício 01 ========================================================")
print("Python na Escola e Programação da Alura.")


# 2 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
# A
# L
# U
# R
# A

print("\nExercício 02 ========================================================")

## O que eu tinha pensado:  print("A\nL\nU\nR\nA\n")
## Maneira mais elegante:
print("A","L","U","R","A",sep="\n")


# 3 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa 
# ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:
# pi = 3.14159

print("\nExercício 03 ========================================================")

pi = 3.14159
print(f"O valor arredondado de pi é: {pi:.2f} \n")
