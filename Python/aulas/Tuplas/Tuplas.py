# Tuplas com números
tupla = (1, 2, 3, 4, 5, 6,0,32,90,84,80)  # (1, 2, 3, 4, 5, 6)

# Tuplas com valores diferentes
tupla2 = (10, "Python", 3.14, [1, 2, 3, 4])  # (10, 'Python', 3.14, [1, 2, 3, 4])

# Adicionando duas tuplas em uma variável
tupla3 = tupla + tupla2  # (1, 2, 3, 4, 5, 6, 10, 'Python', 3.14, [1, 2, 3, 4])

# Adicionando 2 * os valores da tupla
tupla4 = tupla * 2 # 1, 2, 3, 4, 5, 6, 0, 32, 90, 84, 80, 1, 2, 3, 4, 5, 6, 0, 32, 90, 84, 80)

print(tupla)
print(tupla2)
print(tupla3)
print(tupla2[1])
print(tupla4)

print("--------------------")
print("Mostrando o resultado da tupla")
for x in tupla2:
    print(x)



