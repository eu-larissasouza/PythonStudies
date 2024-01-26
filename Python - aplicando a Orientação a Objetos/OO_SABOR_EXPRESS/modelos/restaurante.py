class Restaurante:
    Nome = ""
    Categoria = ""
    Ativo = False


restaurante_praca = Restaurante()
restaurante_praca.Nome = "Praça"
restaurante_praca.Categoria = "Gourmet"

restaurante_pizza = Restaurante()

restaurantes = [restaurante_praca, restaurante_pizza]

# print(dir(restaurante_praca))
print(vars(restaurante_praca))
