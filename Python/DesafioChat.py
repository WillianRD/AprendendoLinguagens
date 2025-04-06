def count():
    # 🧠 DESAFIO 1 – Contador simples
    # # Enunciado:
    # Crie um programa que conte de 1 até 50, mostrando apenas os números pares.
    print("Números pares:")
    for i in range(1,51):
        if i % 2 == 0:
            print(i )

def soma():
# 🧠 DESAFIO 2 – Somando múltiplos
# Enunciado:
# Some todos os múltiplos de 3 entre 1 e 100 e mostre o total no final.
    valor = 0
    for i in range(1, 101):
       if i % 3 == 0:
        print(f"Múltiplo de 3 encontrado: {i}")
        valor += i
    print(f"\nValor total da soma dos múltiplos de 3: {valor}")
        
def tabuada():
    num = int(input('Digite um número para ver a tabuada')) 
    inicio = int(input('Digite o valor inicial do intervalo'))
    fim = int(input('Digite o valor final do intervalo'))
    
    print(f'--- Tabuada de {inicio} até {fim}')
    
    for i in range( inicio, fim + 1):
        resultado = num * i
        print(f'{num} x {i} = {resultado}')

def desenhe():
    # DESAFIO 5 – Desenhando um quadrado com asteriscos
# Enunciado:
# Peça ao usuário um número N e desenhe um quadrado N x N com *.

# 📌 Exemplo para N = 4:

# markdown
# Copiar
# Editar
# ****
# ****
# ****
# ****
    num = int(input('Digite um número para ver o quadrado'))
    for i in range(num):
        print('*' * num)
        
desenhe()        