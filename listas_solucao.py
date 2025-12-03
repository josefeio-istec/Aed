# Soluções dos exercícios de Listas

# Exercício 1
nomes = ["Ana", "Bruno", "Carla", "Daniel", "Eva"]
print(nomes[0])    # primeiro
print(nomes[2])    # terceiro
print(nomes[-1])   # último

# Exercício 2
nomes[1] = "Beatriz"
print(nomes)

# Exercício 3
numeros = [3, 7, 10, 2, 8, 5]

print("Iteração com índice:")
for i in range(len(numeros)):
    print(numeros[i])

print("Iteração sem índice:")
for n in numeros:
    print(n)

# Exercício 4
frutas = ["maçã", "banana", "laranja"]
frutas.append("kiwi")
del frutas[1]
print("Lista de frutas:", frutas)

# Exercício 5
nums = [10, 4, 7, 2, 15, 8, 1, 9, 6, 3]

fatia = nums[2:7]
print("Fatia 2 a 6:", fatia)

invertida = nums[::-1]
print("Invertida:", invertida)

nums.sort()
print("Ordenada:", nums)
