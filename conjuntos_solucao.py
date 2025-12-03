# Soluções dos exercícios de Conjuntos

# Exercício 1
cores = {"vermelho", "verde", "azul", "amarelo", "preto"}
print("Conjunto de cores:", cores)

# Exercício 2
nomes = {"Ana", "Bruno", "Carla"}
# Para evitar bloqueio em ambiente não interativo, o input pode ser comentado.
# nome = input("Digite um nome: ")
# if nome in nomes:
#     print("Nome está no conjunto")
# else:
#     print("Nome não está no conjunto")

# Exercício 3
nomes.add("Daniel")
nomes.add("Eva")
print("Conjunto de nomes:", nomes)

# Exercício 4
valores = {10, 20, 30, 40}
valores.remove(20)
print("Conjunto após remoção:", valores)

# Exercício 5
lista = [1, 2, 2, 3, 3, 3, 4, 1]
conjunto = set(lista)
print("Lista original:", lista)
print("Conjunto sem duplicados:", conjunto)
