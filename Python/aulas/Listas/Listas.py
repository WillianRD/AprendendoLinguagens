nomes = ["WIllian", "Leide" , "Yuri"]
indice = nomes.index("Yuri")
print(nomes)
print(indice)

nomes[0] = "Javeiro"
print(nomes)

nomes.append("Coda fofo")
print(nomes)

nomes.remove("Leide")
print(nomes)

nomes.insert(0,"Coda Fofo")
print(nomes)

numeros = [1,2,3,4,5]
numerosList = [6,7,8,9]

print(3 in numeros)

concatenar = numeros + numerosList
print(concatenar)

number = numeros * 2
print(number)

listaNumerosNaoOrdenado = [1,90,22,55,87,21,9]
listaNumerosNaoOrdenado.sort()
print(listaNumerosNaoOrdenado)

listaNumerosNaoOrdenado.reverse()
print(listaNumerosNaoOrdenado)

list = [1,2,3,4,5]
list.pop()
print(list)
