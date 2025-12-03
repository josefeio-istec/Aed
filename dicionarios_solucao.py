# Soluções dos exercícios de Dicionários

# Exercício 1
pessoas = {
    "ana@gmail.com": "Ana Silva",
    "bruno@gmail.com": "Bruno Costa",
    "carla@gmail.com": "Carla Rocha"
}
print("Nome do email bruno@gmail.com:", pessoas["bruno@gmail.com"])

# Exercício 2
pessoas["daniel@gmail.com"] = "Daniel Sousa"
print("Após adicionar Daniel:", pessoas)

# Exercício 3
pessoas["carla@gmail.com"] = "Carla Rodrigues"
print("Após alterar Carla:", pessoas)

# Exercício 4
del pessoas["bruno@gmail.com"]
print("Após remover Bruno:", pessoas)

# Exercício 5
for chave in pessoas.keys():
    print("chave:", chave)
    print("valor:", pessoas[chave])
