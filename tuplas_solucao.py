# Soluções dos exercícios de Tuplas

# Exercício 1
cidades = ("Lisboa", "Porto", "Coimbra", "Faro")
print(cidades[0])
print(cidades[1])
print(cidades[2])
print(cidades[3])

# Exercício 2
t = (1, 2, 3)
# t[0] = 10  # Isto gera erro: TypeError (tuplas são imutáveis)
# Explicação:
# Tuplas são estruturas imutáveis. Depois de criadas, não é possível
# alterar, adicionar ou remover elementos.

# Exercício 3
t = (5, 10, 15, 20)
lista = list(t)
lista[0] = 50
lista[2] = 150
print("Tupla original:", t)
print("Lista modificada:", lista)

# Exercício 4
pessoas = [("Ana", 20), ("Bruno", 25), ("Carla", 30)]
for nome, idade in pessoas:
    print("Idade:", idade)

# Exercício 5
dados = ("João", 22, "Lisboa")
nome, idade, cidade = dados
print("Nome:", nome)
print("Idade:", idade)
print("Cidade:", cidade)
