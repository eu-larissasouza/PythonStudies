# Mão na massa: classe música

# Crie uma classe Música com os seguintes atributos e crie 3 objetos definindo cada atributo

# nome
# artista
# duracao

print("EXERCICIO - CLASSE MÚSICA ================================\n")


class Musica:
    nome = ""
    artista = ""
    duracao = int  # em segundos


golden_hour = Musica()

golden_hour.nome = "Golden Hour"
golden_hour.artista = "JVKE"
golden_hour.duracao = 217

print(
    f"Música: {golden_hour.nome} - Artista: {golden_hour.artista} - {golden_hour.duracao} segundos"
)

omg = Musica()

omg.nome = "OMG"
omg.artista = "NewJeans"
omg.duracao = 220

print(f"Música: {omg.nome} - Artista: {omg.artista} - {omg.duracao} segundos")


love_lee = Musica()

love_lee.nome = "Love Lee"
love_lee.artista = "AKMU"
love_lee.duracao = 205

print(
    f"Música: {love_lee.nome} - Artista: {love_lee.artista} - {love_lee.duracao} segundos"
)
